# Minecraft Hosting Server with Cloud Automation (BETA / in Progress)

## Java Edition Server (Java and Bedrock Edition Clients can Join the Server)

### [PAPERMC](https://papermc.io/downloads/paper) (host) + [Geyser](https://geysermc.org/download?project=geyser) (required plugin) + [Floodgate](https://geysermc.org/download?project=floodgatehttps://geysermc.org/download?project=floodgate) (required plugin)

The goal with this project is to automate the process of creating a minecraft server with sheduled backups so no data gets lost.

Run this script on new servers to download requrired libraries:

```shell
# sudo apt install pipx -y
sudo snap install astral-uv --classic
uv venv .venv
source .venv/bin/activate
uv pip install .
python3 install_papermc.py
python3 start_papermc.py
deactivate
```

BACKUP:

```shell
python3 papermc_backup.py
# ~/papermc_backup
# ~/papermc_backup_20250000.tar.gz
# tar -xzf ./papermc_backup_20250720.tar.gz
```

Memory note:
```shell
0 3 * * * /home/alex/papermc/.venv/bin/python /home/alex/papermc/backup_script.py >> /home/alex/backup.log 2>&1
```

## Bedrock Edition Server (Only for Bedrock Clients)

### [PocketMineMP](https://github.com/pmmp/PocketMine-MP)
