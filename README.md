# [PAPERMC](https://papermc.io/downloads/paper) Minecraft Server

The goal with this project is to automate the process of creating a minecraft server with sheduled backups so no data gets lost.

Run this script on new servers to download requrired libraries:

```shell
sudo apt install pipx -y
sudo snap install astral-uv --classicuv venv .venv
uv venv .venv
source .venv/bin/activate
uv pip install . 
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
