#!/usr/bin/env python3
"""Real-Life Patch Notes: write one patch-note line to /output/entry.txt."""
import os

# Deterministic: the same single line is written on every run, byte for byte.
# The bug: calling the teacher "mom" in front of the whole class — the mouth
# refuses to issue a correction. Resubmit (round 2): the round-1 line
# (eye floaters, v1.4.7) ranked #1196 of 2197, below the 500 cut — frozen.

LINE = "v1.9.9: fixed a bug where the mouth called the teacher 'mom' in front of 30 classmates and then refused to issue a correction."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
