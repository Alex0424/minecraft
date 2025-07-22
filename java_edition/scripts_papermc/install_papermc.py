#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path
import requests
import json

# --- Get latest supported Minecraft version from PaperMC ---
print("[*] Fetching latest supported Minecraft version...")
version_data = requests.get("https://api.papermc.io/v2/projects/paper").json()
mc_version = version_data["versions"][-1]  # Gets the latest version

# --- Configuration ---
print(f"Latest Minecraft version: {mc_version}")
install_dir = Path.home() / "minecraft-server"
plugins_dir = install_dir / "plugins"
paper_api = f"https://api.papermc.io/v2/projects/paper/versions/{mc_version}"

# --- Ensure directories ---
install_dir.mkdir(parents=True, exist_ok=True)
plugins_dir.mkdir(parents=True, exist_ok=True)

# --- Install system dependencies (run once manually if needed) ---
print("[!] Make sure the following packages are installed: openjdk-17-jre-headless wget unzip screen curl jq")

# --- Get latest Paper build ---
print(f"[*] Fetching latest Paper build for {mc_version}...")
res = requests.get(paper_api)
res.raise_for_status()
builds = res.json()["builds"]
latest_build = builds[-1]
print(f"Latest build: {latest_build}")

# --- Download Paper JAR ---
paper_url = f"{paper_api}/builds/{latest_build}/downloads/paper-{mc_version}-{latest_build}.jar"
paper_jar = install_dir / "paper.jar"
print(f"[*] Downloading Paper: {paper_url}")
with requests.get(paper_url, stream=True) as r:
    if r.status_code != 200:
        print(f"Failed to download Paper jar: HTTP {r.status_code}")
        print(r.text[:500])  # Print first 500 chars of error response
        exit(1)
    with open(paper_jar, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

# --- Accept EULA ---
eula_file = install_dir / "eula.txt"
eula_file.write_text("eula=true\n")
print("[*] EULA accepted")

# --- Download Geyser-Spigot ---
print("[*] Installing Geyser...")
geyser_url = "https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot"
geyser_jar_path = plugins_dir / "Geyser-Spigot.jar"
print(f"[*] Downloading Geyser from {geyser_url}")
with requests.get(paper_url, stream=True) as r:
    r.raise_for_status()
    r.raw.decode_content = True  # force decompress if needed
    with open(paper_jar, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

# --- Download Floodgate-Spigot ---
print("[*] Installing Floodgate...")
floodgate_url = "https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot"
floodgate_jar_path = plugins_dir / "Floodgate-Spigot.jar"
print(f"[*] Downloading Floodgate from {floodgate_url}")
with requests.get(floodgate_url, stream=True) as r:
    r.raise_for_status()
    with open(floodgate_jar_path, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

print(f"[✓] Installation complete in {install_dir}")
