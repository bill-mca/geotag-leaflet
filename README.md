# geotag-leaflet

This is largely adapted from code writen by Jayson DeLancey and available in [this tutorial](https://developer.here.com/blog/getting-started-with-geocoding-exif-image-metadata-in-python3).

geojson_from_exif.py is a script that takes a path to a directory as input and outputs a geojson of all the geotagged jpegs in that folder to the stdout.

generate_thumbnails.py makes a copy of a directory with all jpegs shrunk to thumbnails.

webmap_from_photos.sh takes a path to a directory full of geotagged photos and will generate thumbnails and a json layer compatible with the included index.html template.
