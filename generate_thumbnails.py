#! /usr/bin/python3

from PIL import Image


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

    if len(sys.argv) > 2:
        thumbnail_path = sys.argv[2]
    else:
        thumbnail_path = './tmbs/'

    input_photos = glob.glob(photo_path + '*.jpg') + glob.glob(photo_path + '*.JPG')
    input_photos = [os.path.split(x)[1] for x in input_photos]
    #print(os.getcwd())

    if not os.path.isdir(thumbnail_path):  
        os.mkdir(thumbnail_path)

    for img in input_photos:
      image = Image.open(photo_path + img)
      image.thumbnail((200,200))
      image.save(thumbnail_path + os.path.splitext(img)[0] + '.thumbnail.jpg')

        

