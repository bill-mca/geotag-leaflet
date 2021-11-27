#! /usr/bin/python3

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled

def get_decimal_from_dms(dms, ref):

    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0

    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(
        geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(
        geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)

if __name__ == '__main__':
    import os
    import sys
    import glob
    import json

    #The path of a directory holding the full resolution images to be added
    #to a leaflet map
    if len(sys.argv) > 1:
        photo_path = sys.argv[1]
    else:
        photo_path = './'

    #input_photos = os.listdir(photo_path)
    #j = [os.path.splitext(x)[1].lower() for x in input_photos]
    #print([x for x in j if x == 'jpg'])
    #input_photos = [x for x in input_photos if
    #                os.path.splitext(x)[1].lower() in ['jpg', 'jpeg', 'bmp',
    #                                                   'bitmap', 'tiff']]
    #print(input_photos)
    input_photos = glob.glob(photo_path + '*.jpg') + glob.glob(photo_path + '*.JPG')
    input_photos = [os.path.split(x)[1] for x in input_photos]

    #print(os.getcwd())

    noGPS = []
    tagged = []
    features = []
    for img in input_photos:
        exif = get_exif(photo_path + img)
        try:
            geotags = get_geotagging(exif)
            c = get_coordinates(geotags)
            features.append({
                'type': 'Feature',
                'properties': {
                    'title': '',
                    'name' : img,
                    'description': ''
                    },
                'geometry': {
                    'type': 'Point',
                    'coordinates': [c[1], c[0]]
                }
            })
            tagged.append((img, get_coordinates(geotags)))
        except ValueError:
            noGPS.append(img)
    print(json.dumps({"type": "FeatureCollection",
                      "name": "Photo Points",
                      "crs": {"type": "name",
                              "properties": {
                                  "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                              }
                      },
                      "features": features}))

