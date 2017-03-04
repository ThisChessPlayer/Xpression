import boto3 as b3
import pandas as pd
import sys
import TestRekognition
import json

image_directory = sys.argv[1]
images_list = sys.argv[2]

drivers_df = pd.read_csv(images_list)

drivers_list = []

for i in range(len(5)):#drivers_df['img'])):
    #print(drivers_df['img'][i])#image_directory + "/" + image)
    imageInfo = {}
    #imageInfo['attributes'] = recognizeImage(image_directory + "/" + drivers_df['img'][i])
    imageWrapper = []
    imageWrapper[0] = drivers_df['subject'][i]
    imageInfo['subject'] = drivers_df['subject'][i]
    imageInfo['classname'] = drivers_df['classname'][i]
    imageInfo['imgname'] = drivers_df['img'][i]
    imageWrapper[1] = imageInfo
    print(imageWrapper)
    with open('image_' + str(i), w) as outfile:
        json.dumps(imageWrapper, outfile, indent=4)
