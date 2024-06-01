# GooglePhotosToNextCloud

![googlephotostonextcloud](https://badge.fury.io/py/googlephotstonextcloud.png)

Python tool to migrate Google Photos Takout to NextCloud Photos

## Features

* It doesn't copy the pictures for the Albums, it uses the  Nextcloud Photos albums feature so they are not duplicated
* It supports Memories archive format (.archive)

## Steps

1. Use [Google Photos Takeout Helper](https://github.com/TheLastGimbus/GooglePhotosTakeoutHelper?tab=readme-ov-file#running-manually-with-cmd) to get your Google Takout and apply all the metadata.

```bash
gpth -i <dir containing Takout folder> -o gpth_out --albums=json --no-divide-to-dates
```

2. Upload Takout to NextCloud (it will take a long time. Optionally, you can upload the raw Takout to NextCloud and  then execute the `gpth` command on the server).

3. Use our tool to create the Albums and add the pictures

```bash
python googlephotostonextcloud/main.py
```


## Configuration

The configuration parameters can be found at `config.py`. The documentation can also found there.
