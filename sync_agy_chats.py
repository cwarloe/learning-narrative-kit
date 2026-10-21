#!/usr/bin/env python3
"""Convenience entry point for tools/sync_agy_chats.py"""
import sys
from pathlib import Path

# Add repo root to path
sys.path.insert(0, str(Path(__file__).parent))

from tools.sync_agy_chats import main

if __name__ == "__main__":
    main()
