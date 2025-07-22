#!/usr/bin/env python3

import subprocess

session_name = "minecraft"

# Check if the screen session exists
try:
    output = subprocess.check_output(["screen", "-ls"], stderr=subprocess.DEVNULL).decode()
    if session_name not in output:
        print(f"[!] No screen session named '{session_name}' is running.")
        exit(1)
except subprocess.CalledProcessError:
    print("[!] Failed to check screen sessions. Is 'screen' installed?")
    exit(1)

# Send the stop command to gracefully shut down the Minecraft server
print(f"[*] Stopping PaperMC server in screen session '{session_name}'...")
try:
    subprocess.run(["screen", "-S", session_name, "-p", "0", "-X", "stuff", "stop\n"], check=True)
    print("[✓] Stop command sent. Server will shut down shortly.")
except subprocess.CalledProcessError:
    print("[!] Failed to send stop command to the screen session.")

