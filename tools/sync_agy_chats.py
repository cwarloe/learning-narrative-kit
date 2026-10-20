#!/usr/bin/env python3
"""
Antigravity CLI / IDE Chat Sync Tool
------------------------------------
Export and import chat sessions, history, and transcripts between machines.

Features:
- Standard library only (zero external dependencies).
- Safe read-only SQLite snapshotting (handles active WAL logs).
- Merges conversations into the destination machine without overwriting other chats.
- Cross-platform: works across Windows, macOS, and Linux.

Usage:
  # 1. On your current machine:
  python sync_agy_chats.py list
  python sync_agy_chats.py export --out my_chats.zip          # Export all conversations
  python sync_agy_chats.py export --last 5 --out recent.zip   # Export last 5 conversations
  python sync_agy_chats.py export --id <conv-id>              # Export a specific conversation

  # 2. On your other computer:
  python sync_agy_chats.py import my_chats.zip
  agy --continue
"""

import argparse
import json
import os
import shutil
import sqlite3
import sys
import zipfile
from datetime import datetime
from pathlib import Path


def get_default_antigravity_dir() -> Path:
    return Path.home() / ".gemini" / "antigravity"


def get_ro_connection(db_path: Path):
    if not db_path.exists():
        return None
    # Connect with read-only URI mode to prevent locking issues with active sessions
    conn_uri = f"file:{db_path.as_posix()}?mode=ro"
    conn = sqlite3.connect(conn_uri, uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def list_conversations(antigravity_dir: Path, limit: int = 15):
    db_path = antigravity_dir / "conversation_summaries.db"
    conn = get_ro_connection(db_path)
    if not conn:
        print(f"[!] No conversation database found at: {db_path}")
        return

    try:
        rows = conn.execute(
            """
            SELECT conversation_id, title, last_modified_time, step_count
            FROM conversation_summaries
            ORDER BY last_modified_time DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()

        if not rows:
            print("No conversations found.")
            return

        print(f"\nConversations in {antigravity_dir} (showing up to {limit}):")
        print(f"{'#':<3} | {'Conversation ID':<36} | {'Steps':<5} | {'Modified (UTC)':<19} | {'Title'}")
        print("-" * 100)
        for idx, r in enumerate(rows, 1):
            title = r["title"] or "(Untitled)"
            mod_time = str(r["last_modified_time"])[:19]
            print(f"{idx:<3} | {r['conversation_id']} | {r['step_count']:<5} | {mod_time} | {title}")
        print()
    finally:
        conn.close()


def export_bundle(antigravity_dir: Path, out_zip: Path, conv_id: str = None, last_n: int = None):
    db_path = antigravity_dir / "conversation_summaries.db"
    conn = get_ro_connection(db_path)
    if not conn:
        print(f"[!] Error: {db_path} not found.")
        sys.exit(1)

    try:
        if conv_id:
            rows = conn.execute(
                "SELECT * FROM conversation_summaries WHERE conversation_id = ?",
                (conv_id,),
            ).fetchall()
        elif last_n:
            rows = conn.execute(
                "SELECT * FROM conversation_summaries ORDER BY last_modified_time DESC LIMIT ?",
                (last_n,),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM conversation_summaries ORDER BY last_modified_time DESC"
            ).fetchall()

        if not rows:
            print("[!] No matching conversations found to export.")
            return

        export_ids = [r["conversation_id"] for r in rows]
        print(f"[*] Packaging {len(export_ids)} conversation(s)...")

        # Create temporary SQLite DB to store extracted summary records
        temp_dir = Path.cwd() / ".agy_sync_tmp"
        temp_dir.mkdir(parents=True, exist_ok=True)
        tmp_db_path = temp_dir / "conversation_summaries.db"
        if tmp_db_path.exists():
            tmp_db_path.unlink()

        dest_conn = sqlite3.connect(str(tmp_db_path))
        schema_row = conn.execute(
            "SELECT sql FROM sqlite_master WHERE type='table' AND name='conversation_summaries'"
        ).fetchone()
        if schema_row and schema_row[0]:
            dest_conn.execute(schema_row[0])

        cols = [col[0] for col in conn.execute("SELECT * FROM conversation_summaries LIMIT 1").description]
        placeholders = ",".join(["?"] * len(cols))
        col_names = ",".join([f"`{c}`" for c in cols])

        for r in rows:
            dest_conn.execute(
                f"INSERT OR REPLACE INTO conversation_summaries ({col_names}) VALUES ({placeholders})",
                tuple(r),
            )
        dest_conn.commit()
        dest_conn.close()

        # Build ZIP archive
        out_zip_resolved = out_zip.resolve()
        with zipfile.ZipFile(str(out_zip), "w", zipfile.ZIP_DEFLATED) as zf:
            meta = {
                "created_at": datetime.utcnow().isoformat(),
                "conversation_ids": export_ids,
                "count": len(export_ids),
            }
            zf.writestr("metadata.json", json.dumps(meta, indent=2))
            zf.write(str(tmp_db_path), "conversation_summaries.db")

            conversations_dir = antigravity_dir / "conversations"
            brain_dir = antigravity_dir / "brain"

            for cid in export_ids:
                # 1. Conversation SQLite DB
                conv_file = conversations_dir / f"{cid}.db"
                if conv_file.exists():
                    try:
                        zf.write(str(conv_file), f"conversations/{cid}.db")
                    except Exception as e:
                        print(f"  [!] Skipped {conv_file.name}: {e}")

                # 2. Brain directory (logs, transcripts, artifacts)
                cid_brain_dir = brain_dir / cid
                if cid_brain_dir.exists():
                    for root, _, files in os.walk(str(cid_brain_dir)):
                        for f in files:
                            # Skip zip files or temporary lock files
                            if f.endswith(".zip") or f.endswith(".lock"):
                                continue
                            full_path = Path(root) / f
                            if full_path.resolve() == out_zip_resolved:
                                continue
                            rel_path = full_path.relative_to(brain_dir)
                            try:
                                zf.write(str(full_path), f"brain/{rel_path.as_posix()}")
                            except Exception:
                                pass

        # Clean up temp
        shutil.rmtree(temp_dir, ignore_errors=True)

        size_mb = out_zip.stat().st_size / (1024 * 1024)
        print(f"\n[+] Successfully exported {len(export_ids)} conversation(s) to:")
        print(f"    {out_zip.resolve()} ({size_mb:.2f} MB)")
        print("\nNext steps:")
        print(f"  1. Transfer '{out_zip.name}' (and this script) to your other computer.")
        print(f"  2. Run: python sync_agy_chats.py import {out_zip.name}")
        print("  3. Run: agy --continue")

    finally:
        conn.close()


def import_bundle(zip_path: Path, antigravity_dir: Path):
    if not zip_path.exists():
        print(f"[!] Error: Archive '{zip_path}' not found.")
        sys.exit(1)

    antigravity_dir.mkdir(parents=True, exist_ok=True)
    target_conv_dir = antigravity_dir / "conversations"
    target_brain_dir = antigravity_dir / "brain"
    target_conv_dir.mkdir(exist_ok=True)
    target_brain_dir.mkdir(exist_ok=True)

    target_db_path = antigravity_dir / "conversation_summaries.db"

    with zipfile.ZipFile(str(zip_path), "r") as zf:
        namelist = zf.namelist()
        if "metadata.json" not in namelist:
            print("[!] Error: Invalid bundle (missing metadata.json).")
            sys.exit(1)

        meta = json.loads(zf.read("metadata.json").decode("utf-8"))
        conv_ids = meta.get("conversation_ids", [])
        print(f"[*] Importing {len(conv_ids)} conversation(s) into: {antigravity_dir}...")

        # Extract conversations & brain files
        for name in namelist:
            if name.startswith("conversations/") and name.endswith(".db"):
                filename = Path(name).name
                dest = target_conv_dir / filename
                with zf.open(name) as src, open(dest, "wb") as dst:
                    shutil.copyfileobj(src, dst)
            elif name.startswith("brain/"):
                rel_parts = Path(name).parts[1:]
                if not rel_parts:
                    continue
                dest = target_brain_dir.joinpath(*rel_parts)
                dest.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(name) as src, open(dest, "wb") as dst:
                    shutil.copyfileobj(src, dst)

        # Merge conversation_summaries.db
        if "conversation_summaries.db" in namelist:
            temp_db = antigravity_dir / "temp_imported_summaries.db"
            with zf.open("conversation_summaries.db") as src, open(temp_db, "wb") as dst:
                shutil.copyfileobj(src, dst)

            if not target_db_path.exists():
                shutil.move(str(temp_db), str(target_db_path))
                print("[+] Initialized conversation_summaries.db on target.")
            else:
                src_conn = sqlite3.connect(str(temp_db))
                src_conn.row_factory = sqlite3.Row
                dst_conn = sqlite3.connect(str(target_db_path))

                rows = src_conn.execute("SELECT * FROM conversation_summaries").fetchall()
                if rows:
                    cols = [col[0] for col in src_conn.execute("SELECT * FROM conversation_summaries LIMIT 1").description]
                    placeholders = ",".join(["?"] * len(cols))
                    col_names = ",".join([f"`{c}`" for c in cols])

                    for r in rows:
                        dst_conn.execute(
                            f"INSERT OR REPLACE INTO conversation_summaries ({col_names}) VALUES ({placeholders})",
                            tuple(r),
                        )
                    dst_conn.commit()
                src_conn.close()
                dst_conn.close()
                if temp_db.exists():
                    temp_db.unlink()
                print("[+] Merged imported conversation index without overwriting existing chats.")

    print(f"\n[+] Done! Imported {len(conv_ids)} conversation(s).")
    if conv_ids:
        print("\nTo resume in the CLI on this computer:")
        print("  agy --continue                       # Resume most recent chat")
        print(f"  agy --conversation {conv_ids[0]}     # Resume specific chat")


def main():
    parser = argparse.ArgumentParser(description="Antigravity Chat Sync Tool")
    parser.add_argument(
        "--dir",
        type=Path,
        default=get_default_antigravity_dir(),
        help="Antigravity data directory (default: ~/.gemini/antigravity)",
    )
    subparsers = parser.add_subparsers(dest="command")

    # list
    p_list = subparsers.add_parser("list", help="List local conversations")
    p_list.add_argument("-n", "--limit", type=int, default=15, help="Number of items to show")
    p_list.add_argument("--dir", type=Path, default=None, help=argparse.SUPPRESS)

    # export
    p_export = subparsers.add_parser("export", help="Export conversations to a zip bundle")
    p_export.add_argument("-o", "--out", type=Path, default=Path("agy_chats.zip"), help="Output zip file path")
    p_export.add_argument("--id", dest="conv_id", type=str, help="Export a specific conversation ID")
    p_export.add_argument("-n", "--last", type=int, help="Export the last N conversations")
    p_export.add_argument("--dir", type=Path, default=None, help=argparse.SUPPRESS)

    # import
    p_import = subparsers.add_parser("import", help="Import conversations from a zip bundle")
    p_import.add_argument("archive", type=Path, help="Path to zip bundle created by export")
    p_import.add_argument("--dir", type=Path, default=None, help=argparse.SUPPRESS)

    args = parser.parse_args()
    target_dir = getattr(args, "dir", None) or get_default_antigravity_dir()

    if args.command == "list":
        list_conversations(target_dir, limit=args.limit)
    elif args.command == "export":
        export_bundle(target_dir, args.out, conv_id=args.conv_id, last_n=args.last)
    elif args.command == "import":
        import_bundle(args.archive, target_dir)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
