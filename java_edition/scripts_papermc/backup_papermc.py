#!/usr/bin/env python3

from pathlib import Path
import shutil
import tarfile
from datetime import datetime

# --- Configuration ---
source_dir = Path.home() / "minecraft-server"
backup_dir = Path.home() / "papermc_backup"
compress = True

excluded_dirs = {"logs", "cache"}
excluded_files = {"paper.jar"}
excluded_prefixes = {"hs_err_pid"}

# --- Ensure backup directory exists ---
backup_dir.mkdir(parents=True, exist_ok=True)

# --- Copy files selectively ---
for src_file in source_dir.rglob("*"):
    if src_file.is_dir():
        continue

    rel_path = src_file.relative_to(source_dir)

    # Skip files in excluded directories
    if any(part in excluded_dirs for part in rel_path.parts):
        continue

    # Skip excluded files
    if src_file.name in excluded_files or any(src_file.name.startswith(p) for p in excluded_prefixes):
        continue

    dest_file = backup_dir / rel_path
    dest_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_file, dest_file)

print(f"Backup copied to {backup_dir}")

# --- Compress backup ---
if compress:
    timestamp = datetime.now().strftime("%Y%m%d")
    tar_path = backup_dir.with_name(f"{backup_dir.name}_{timestamp}.tar.gz")
    with tarfile.open(tar_path, "w:gz") as tar:
        tar.add(backup_dir, arcname=backup_dir.name)
    print(f"Backup compressed to {tar_path}")

# Save to Amazon S3 bucket in near future
