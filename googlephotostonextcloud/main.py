import json
from tqdm import tqdm

from googlephotostonextcloud.nextcloud_api import NextCloudAPI
import googlephotostonextcloud.config as config

# https://github.com/nextcloud/photos/pull/2172

def main():

    nclient = NextCloudAPI(config.NC_URL, config.NC_USER, config.NC_PASS, config.OCC_CMD_F)
    
    text = nclient.get_file(config.GPTH_JSON_FILE)
    json_data = json.loads(text)

    if config.CREATE_ALBUMS:
        albums = [albums for _, albums in json_data.items()]
        albums = list(set([item for sublist in albums for item in sublist]))
        
        for album in tqdm(albums):
            nclient.run_occ(f'photos:album:create {config.NC_USER} \\"{album}\\"')

    batches = [
        [f'photos:album:add {config.NC_USER} \\"{album}\\" \\"{config.GPTH_PATH}/ALL_PHOTOS/{p_name}\\"' for album in albums]
        for p_name, albums in json_data.items()
    ]
    batches = list([item for sublist in batches for item in sublist])
    
    for i in tqdm(range(0, len(batches), config.BATCH_SIZE)):
        batch = batches[i:i+config.BATCH_SIZE]
        nclient.run_occs(batch)

    # for p_name, albums in tqdm(json_data.items()):
    #     for album in albums:
    #         nclient.run_occ(f'photos:album:add {NC_USER} \\"{album}\\" \\"{GPTH_PATH}/ALL_PHOTOS/{p_name}\\"')
    
if __name__ == '__main__':
    main()