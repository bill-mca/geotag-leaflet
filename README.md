# geotag-leaflet

The purpose of this code is to allow me to quickly generate a map of a landscape following a site visit. I intend to be able to download photos from my phone and drone and use this tool to create a leaflet map in 10 minutes. these webmaps could be deployed to my website by another script for a rapid turnaround on a site assessment.

## Attribution
This is largely adapted from code writen by Jayson DeLancey and available in [this tutorial](https://developer.here.com/blog/getting-started-with-geocoding-exif-image-metadata-in-python3).

## Instructions
geojson_from_exif.py is a script that takes a path to a directory as input and outputs a geojson of all the geotagged jpegs in that folder to the stdout.

generate_thumbnails.py makes a copy of a directory with all jpegs shrunk to thumbnails.

webmap_from_photos.sh takes a path to a directory full of geotagged photos and will generate thumbnails and a json layer compatible with the included index.html template.

## Future Development
- Improve the html and javascript to make the final output look more pleasant
    - Give elements varying degrees of significance that is represented by opacity/scale of their icon
- Enable a bit of customisation by allowing a title and description to be added to each photopoint
- Replace the bash code with python so that the code is cross-platform
- a script to automatically upload to S3
