#!/usr/bin/env python3
"""Thin wrapper: render this unit via tools/render_unit.py (also writes local scratch HTML)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KIT_ROOT = ROOT.parent.parent
sys.path.insert(0, str(KIT_ROOT / "tools"))

from render_unit import render_unit  # noqa: E402

if __name__ == "__main__":
    render_unit(
        ROOT,
        kit_root=KIT_ROOT,
        also_local=ROOT / "portland-desk.html",
    )
