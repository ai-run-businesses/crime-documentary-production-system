#!/usr/bin/env python3
"""Create regular and scene-change frame samples plus a contact sheet for video QA."""

from __future__ import annotations

import argparse
import csv
import json
import math
import shutil
import subprocess
from pathlib import Path


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, text=True, capture_output=True)


def probe(path: Path) -> dict[str, float | int | str]:
    data = json.loads(run([
        "ffprobe", "-v", "error", "-show_streams", "-show_format",
        "-of", "json", str(path),
    ]).stdout)
    video = next(stream for stream in data["streams"] if stream["codec_type"] == "video")
    audio = next((stream for stream in data["streams"] if stream["codec_type"] == "audio"), None)
    return {
        "duration": float(data["format"]["duration"]),
        "width": int(video["width"]),
        "height": int(video["height"]),
        "video_codec": video.get("codec_name", ""),
        "audio_codec": audio.get("codec_name", "") if audio else "",
    }


def timestamp_name(seconds: float) -> str:
    return f"{seconds:08.3f}".replace(".", "_") + ".jpg"


def extract(path: Path, seconds: float, target: Path) -> None:
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-ss", f"{seconds:.3f}", "-i", str(path), "-frames:v", "1",
        "-vf", "scale=480:-2", "-q:v", "2", str(target),
    ], check=True)


def scene_times(path: Path, threshold: float) -> list[float]:
    proc = subprocess.run([
        "ffmpeg", "-hide_banner", "-i", str(path),
        "-vf", f"select='gt(scene,{threshold})',showinfo", "-f", "null", "-",
    ], text=True, capture_output=True)
    times: list[float] = []
    for line in proc.stderr.splitlines():
        marker = "pts_time:"
        if marker not in line:
            continue
        value = line.split(marker, 1)[1].split()[0]
        try:
            times.append(float(value))
        except ValueError:
            pass
    return times


def contact_sheet(frames: list[Path], output: Path, columns: int = 4) -> None:
    if not frames:
        return
    rows = math.ceil(len(frames) / columns)
    subprocess.run([
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-pattern_type", "glob", "-i", str(frames[0].parent / "*.jpg"),
        "-vf", f"tile={columns}x{rows}:padding=4:margin=4:color=black",
        "-frames:v", "1", str(output),
    ], check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("video", type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--interval", type=float, default=5.0)
    parser.add_argument("--scene-threshold", type=float, default=0.35)
    parser.add_argument("--max-scenes", type=int, default=80)
    args = parser.parse_args()

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise SystemExit("ffmpeg and ffprobe are required")
    if not args.video.exists():
        raise SystemExit(f"Video not found: {args.video}")

    args.out.mkdir(parents=True, exist_ok=True)
    regular_dir = args.out / "regular"
    scene_dir = args.out / "scene_changes"
    regular_dir.mkdir(exist_ok=True)
    scene_dir.mkdir(exist_ok=True)

    metadata = probe(args.video)
    duration = float(metadata["duration"])
    regular_times = [min(t, max(0.0, duration - 0.05)) for t in
                     [i * args.interval for i in range(math.ceil(duration / args.interval))]]
    scenes = scene_times(args.video, args.scene_threshold)[: args.max_scenes]

    rows: list[tuple[str, float, str]] = []
    regular_frames: list[Path] = []
    scene_frames: list[Path] = []
    for kind, times, folder, bucket in (
        ("regular", regular_times, regular_dir, regular_frames),
        ("scene_change", scenes, scene_dir, scene_frames),
    ):
        for value in times:
            target = folder / timestamp_name(value)
            extract(args.video, value, target)
            bucket.append(target)
            rows.append((kind, value, str(target)))

    contact_sheet(regular_frames, args.out / "regular-contact-sheet.jpg")
    contact_sheet(scene_frames, args.out / "scene-change-contact-sheet.jpg")
    with (args.out / "frames.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["kind", "seconds", "path"])
        writer.writerows(rows)
    (args.out / "manifest.json").write_text(json.dumps({
        "video": str(args.video.resolve()),
        "metadata": metadata,
        "regular_interval_seconds": args.interval,
        "scene_threshold": args.scene_threshold,
        "regular_frame_count": len(regular_frames),
        "scene_frame_count": len(scene_frames),
        "manual_review_required": [
            "unwanted source text or watermarks",
            "wrong-person imagery",
            "sub-1.5-second information shots",
            "caption collisions",
            "generated pseudo-text",
        ],
    }, indent=2) + "\n")


if __name__ == "__main__":
    main()
