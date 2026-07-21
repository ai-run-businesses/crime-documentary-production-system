#!/usr/bin/env python3
"""Inspect technical, loudness, checksum, and final-frame state of a brand intro."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import subprocess
from pathlib import Path


def run(command: list[str]) -> str:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return result.stdout + result.stderr


def checksum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def probe(path: Path) -> dict:
    return json.loads(
        run(
            [
                "ffprobe", "-v", "error", "-show_entries",
                "format=duration,size,bit_rate:stream=index,codec_type,codec_name,width,height,r_frame_rate,sample_rate,channels",
                "-of", "json", str(path),
            ]
        )
    )


def loudness(path: Path) -> dict:
    output = run(
        [
            "ffmpeg", "-hide_banner", "-nostats", "-i", str(path),
            "-filter_complex", "ebur128=peak=true", "-f", "null", "-",
        ]
    )
    integrated = re.findall(r"I:\s+(-?[0-9.]+) LUFS", output)
    peaks = re.findall(r"Peak:\s+(-?[0-9.]+) dBFS", output)
    return {
        "integrated_lufs": float(integrated[-1]) if integrated else None,
        "true_peak_dbfs": float(peaks[-1]) if peaks else None,
    }


def tail_signal(path: Path, metadata_file: Path) -> list[float]:
    run(
        [
            "ffmpeg", "-hide_banner", "-y", "-sseof", "-0.25", "-i", str(path),
            "-vf", f"signalstats,metadata=print:file={metadata_file}",
            "-an", "-f", "null", "-",
        ]
    )
    values = []
    for line in metadata_file.read_text().splitlines():
        if line.startswith("lavfi.signalstats.YAVG="):
            values.append(float(line.split("=", 1)[1]))
    return values


def make_tail_sheet(path: Path, output: Path) -> None:
    run(
        [
            "ffmpeg", "-hide_banner", "-y", "-sseof", "-0.10", "-i", str(path),
            "-vf", "fps=30,scale=640:-1,tile=3x1:padding=4:margin=4",
            "-frames:v", "1", "-update", "1", str(output),
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    video = args.video.resolve()
    out = (args.out or video.parent / f"{video.stem}-qa").resolve()
    out.mkdir(parents=True, exist_ok=True)

    media = probe(video)
    audio = loudness(video)
    yavg = tail_signal(video, out / "tail-signalstats.txt")
    make_tail_sheet(video, out / "final-three-frames.jpg")

    video_streams = [s for s in media.get("streams", []) if s.get("codec_type") == "video"]
    audio_streams = [s for s in media.get("streams", []) if s.get("codec_type") == "audio"]
    prior = yavg[:-1]
    baseline = statistics.median(prior) if prior else None
    final_luma = yavg[-1] if yavg else None
    collapsed_tail = bool(
        baseline is not None
        and final_luma is not None
        and baseline > 0.5
        and final_luma < baseline * 0.40
    )

    failures = []
    if not video_streams:
        failures.append("missing video stream")
    if not audio_streams:
        failures.append("missing audio stream")
    if collapsed_tail:
        failures.append("final frame luminance collapsed relative to preceding frames")
    if audio["true_peak_dbfs"] is not None and audio["true_peak_dbfs"] > -0.5:
        failures.append("insufficient true-peak margin")

    report = {
        "video": str(video),
        "status": "pass" if not failures else "fail",
        "sha256": checksum(video),
        "media": media,
        "loudness": audio,
        "tail": {
            "sample_count": len(yavg),
            "yavg": yavg,
            "baseline_yavg": baseline,
            "final_yavg": final_luma,
            "collapsed_tail": collapsed_tail,
            "contact_sheet": str(out / "final-three-frames.jpg"),
        },
        "failures": failures,
        "manual_gates": [
            "watch the complete export with sound",
            "inspect the final three frames at original resolution",
            "confirm full wordmark and CTA remain present through the last frame",
            "confirm narration, captions, picture, and ending sting are synchronized",
        ],
    }
    (out / "report.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
