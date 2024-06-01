# GooglePhotosToNextCloud

![googlephotostonextcloud](https://badge.fury.io/py/googlephotstonextcloud.png)
![build](https://travis-ci.org/marcbenedi/googlephotostonextcloud.png?branch=master)

Python tool to migrate Google Photos Takout to NextCloud Photos

## Features

* It doesn't copy the pictures for the Albums, it uses the  Nextcloud Photos albums feature so they are not duplicated
* It supports Memories archive format (.archive)

## TODO

- .archive compatible with Memories

## Steps

1. Request Google Takout of Photos
2. Upload takout the nextcloud (will take forever)
3. Extract using https://github.com/TheLastGimbus/GooglePhotosTakeoutHelper?tab=readme-ov-file#running-manually-with-cmd
4. Use script to convert processed takout to Photos Nextcloud
5. Remove remaining shit
6. occ scann files

## Configuration

