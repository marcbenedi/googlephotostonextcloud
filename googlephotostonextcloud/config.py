import os
from getpass import getpass

NC_URL: str = "https://nextcloudaio.homelab.marcb.pro"
NC_USER: str = "marc"
NC_PASS: str = os.getenv('NC_PASS') if os.getenv('NC_PASS') else getpass('Enter NC_PASS: ')
# NC_PASS: str = ""

# Location of the Google Photos Takeout Helper folder in Nextcloud
GPTH_PATH: str = "gpth_out"

# Update the OCC_CMD to match your Nextcloud installation (e.g. docker exec, occ path, etc.)
OCC_CMD: str = "sudo docker exec --user www-data -it nextcloud-aio-nextcloud php occ -n"

# Set to True if Nextcloud is running on a remote server
IS_REMOTE: bool = True

# If IS_REMOTE is True, set the remote host (e.g. user@hostname)
REMOTE_HOST: str = "root@omv"

# Set to True to create albums in Nextcloud (should be True unless you have already created the albums)
CREATE_ALBUMS: bool = False

# Number of occ commands to run at the same time (speeds up the migration, specially for remote servers)
BATCH_SIZE: int = 100


# DO NOT TOUCH
# Adjust values according to configuration
# <-
if IS_REMOTE:
    # We will use SSH to connect to the remote server and execute occ command
    # Configure the remote host with passwordless SSH (for example. using SSH keys)
    OCC_CMD_F = lambda cmd: f"ssh -t {REMOTE_HOST} \"{OCC_CMD} {cmd}\""
else:
    OCC_CMD_F = lambda cmd: f"{OCC_CMD} {cmd}"
    
GPTH_JSON_FILE = f"{GPTH_PATH}/albums-info.json"
# ->