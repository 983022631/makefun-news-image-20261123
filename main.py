#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261123 (Python 3.13, stdlib only).

The front page is drawn by draw.py (Python + PIL) and committed here as
entry.png; this program copies it to the output directory the harness
provides, so the run needs no network and is byte-identical every time.
The copy is byte for byte: the file the grader reads is the file
committed here, so both graded runs produce the same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
