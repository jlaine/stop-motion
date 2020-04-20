#!/usr/bin/env python

import subprocess

subprocess.check_call(
    [
        "ffmpeg",
        "-r",
        "6",
        "-i",
        "images/capt%04d.jpg",
        "-vf",
        "scale=1404:-1",
        "-pix_fmt",
        "yuv420p",
        "-r",
        "24",
        "-strict",
        "-2",
        "-movflags",
        "faststart",
        "bob4.mp4",
    ]
)
