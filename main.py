#!/usr/bin/env python3
"""Real-Life Patch Notes: write one patch-note line to /output/entry.txt."""
import os

# Deterministic: the same single line is written on every run, byte for byte.
# The bug: eye floaters — a tiny transparent worm that follows the gaze
# and dodges every attempt to look at it.

LINE = "v1.4.7: fixed a bug where the eyes rendered a tiny transparent worm that follows the user's gaze and dodges every attempt to look at it."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
