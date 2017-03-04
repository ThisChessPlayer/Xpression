import boto3 as b3
import pandas as pd
import sys
import TestRekognition

image_directory = sys.argv[1]
images_list = sys.argv[2]

drivers_df = pd.read_csv(images_list)

for i in range(len(drivers_df['img'])):
    print(drivers_df['img'][i])#image_directory + "/" + image)
    imageInfo = {}
    #imageInfo['attributes'] = recognizeImage(image_directory + "/" + drivers_df['img'][i])
    imageInfo['subject'] = drivers_df['subject'][i]
    imageInfo['classname'] = drivers_df['classname'][i]
    imageInfo['imgname'] = drivers_df['img'][i]
    print(imageInfo)
