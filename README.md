# GooglePhotosToNextCloud

![googlephotostonextcloud](https://badge.fury.io/py/googlephotstonextcloud.png)

Python tool to migrate Google Photos Takout to NextCloud Photos.

## Features

* It creates the Albums in NextCloud Photos data base (therefore, not as folders)
* It does not copy the image files to the albums, it just add the image to the album (no data duplication).


## Steps

1. Use [Google Photos Takeout Helper](https://github.com/TheLastGimbus/GooglePhotosTakeoutHelper?tab=readme-ov-file#running-manually-with-cmd) to get your Google Takout and apply all the metadata.

```bash
gpth -i <dir containing Takout folder> -o gpth_out --albums=json --no-divide-to-dates
```

2. Upload Takout to NextCloud (it will take a long time. Optionally, you can upload the raw Takout to NextCloud and  then execute the `gpth` command on the server).

```bash
rclone copy gpth_out nextcloud:gpth_out --update --progress
```

3. Use our tool to create the Albums and add the pictures

```bash
python googlephotostonextcloud/main.py
```

## Configuration

The configuration parameters can be found at `config.py`. The documentation can also found there.
