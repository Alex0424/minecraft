#!/usr/bin/env python3

import subprocess
from pathlib import Path

install_dir = Path.home() / "minecraft-server"
paper_jar = install_dir / "paper.jar"

if not paper_jar.exists():
    print("[!] paper.jar not found. Please run install_papermc.py first.")
    exit(1)

# Start in screen session named "minecraft"
print("[*] Starting server in screen session 'minecraft'...")
subprocess.run([
    "screen", "-dmS", "minecraft",
    "java", "-Xms2G", "-Xmx4G", "-jar", "paper.jar", "nogui"
], cwd=install_dir)

print("[✓] Server started. Use: screen -r minecraft")
