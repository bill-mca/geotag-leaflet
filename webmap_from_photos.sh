#! /bin/bash

mkdir full_res/
cp $1*.jpg full_res/
cp $1*.JPG full_res/

echo var photopoints =  > photopoints.js
python3 geojson_from_exif.py $1 >> photopoints.js

python3 generate_thumbnails.py full_res/ tmbs/

