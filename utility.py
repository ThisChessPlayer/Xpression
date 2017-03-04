import boto3 as b3
import pandas as pd
import sys
import TestRekognition
import os

def getImageInfo(image_directory, images_list, index):

    drivers_df = pd.read_csv(images_list)

    drivers_list = []

    filename = image_directory + "/train/" + drivers_df['classname'][index] + "/"+ drivers_df['img'][index]
    print(filename)
    if (not os.path.isfile(str(filename))):
        filename = image_directory + "/test/" + drivers_df['img'][index]
    imageInfo = {}
    imageInfo['attributes'] = TestRekognition.recognizeImage(filename)
    imageWrapper = []
    imageWrapper.append(drivers_df['subject'][index])
    imageInfo['subject'] = drivers_df['subject'][index]
    imageInfo['classname'] = drivers_df['classname'][index]
    imageInfo['imgname'] = drivers_df['img'][index]
    imageWrapper.append(imageInfo)
    print(imageWrapper)
    return imageWrapper
