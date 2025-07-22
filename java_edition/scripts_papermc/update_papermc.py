#!/usr/bin/env python3

import requests

PROJECT = "paper"
USER_AGENT = "AlexBot/v1 (https://alexanderlindholm.net)"
API = f"https://fill.papermc.io/v3/projects/{PROJECT}"
HEADERS = {"User-Agent": USER_AGENT}

# 1. Get the latest Minecraft version supported by Paper
response = requests.get(API, headers=HEADERS)
response.raise_for_status()

data = response.json()
all_versions = []

for version_group in data["versions"].values():
    all_versions.extend(version_group)

# CHECK MANUALLY: curl -s -H "User-Agent: Alex" "https://fill.papermc.io/v3/projects/paper" | jq -r '.versions'
latest_ver = all_versions[0]

print(f"Latest Minecraft version: {latest_ver}")


