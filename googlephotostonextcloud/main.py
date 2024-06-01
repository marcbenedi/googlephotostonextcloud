import json
import os
from getpass import getpass
from tqdm import tqdm

from googlephotostonextcloud.nextcloud_api import NextCloudAPI


# Configuration parameters
# <-
NC_URL: str = "https://nextcloudaio.homelab.marcb.pro"
NC_USER: str = "marc"
NC_PASS: str = os.getenv('NC_PASS') if os.getenv('NC_PASS') else getpass('Enter NC_PASS: ')
# NC_PASS: str = ""

# https://github.com/pulsejet/memories
# NC_MEMORIES: bool = False # Will store the ARCHIVE folder to .archive

# GPT_ARCHIVE_FOLDER: str = "Arxiu" # Archive (Depends on your language)
GPTH_PATH: str = "gpth_out"
# NC_PHOTOS_PATH: str = "photos"

# Update the OCC_CMD to match your Nextcloud installation (e.g. docker exec, occ path, etc.)
OCC_CMD: str = "sudo docker exec --user www-data -it nextcloud-aio-nextcloud php occ -n"

IS_REMOTE: bool = True
REMOTE_HOST: str = "root@omv"

CREATE_ALBUMS: bool = False
BATCH_SIZE: int = 10
# ->


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

# https://github.com/nextcloud/photos/pull/2172

def main():

    nclient = NextCloudAPI(NC_URL, NC_USER, NC_PASS, OCC_CMD_F)
    
    text = nclient.get_file(GPTH_JSON_FILE)
    json_data = json.loads(text)

    if CREATE_ALBUMS:
        albums = [albums for _, albums in json_data.items()]
        albums = list(set([item for sublist in albums for item in sublist]))
        
        for album in tqdm(albums):
            output = nclient.run_occ(f'photos:album:create {NC_USER} \\"{album}\\"')

    batches = [
        [f'photos:album:add {NC_USER} \\"{album}\\" \\"{GPTH_PATH}/ALL_PHOTOS/{p_name}\\"' for album in albums]
        for p_name, albums in json_data.items()
    ]
    batches = list([item for sublist in batches for item in sublist]) # Flatten list
    
    for i in tqdm(range(0, len(batches), BATCH_SIZE)):
        batch = batches[i:i+BATCH_SIZE]
        output = nclient.run_occs(batch)

    # for p_name, albums in tqdm(json_data.items()):
    #     for album in albums:
    #         output = nclient.run_occ(f'photos:album:add {NC_USER} \\"{album}\\" \\"{GPTH_PATH}/ALL_PHOTOS/{p_name}\\"')
    
if __name__ == '__main__':
    main()