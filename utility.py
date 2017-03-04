import boto3 as b3
import pandas as pd
import sys
import RekognitionInterface
import os
import csv
import json

def getImageInfo(drivers_df, image_directory, images_list, index):

    #drivers_df = pd.read_csv(images_list)

    filename = image_directory + "/train/" + drivers_df['classname'][index] + "/"+ drivers_df['img'][index]
    print(filename)
    if (not os.path.isfile(str(filename))):
        filename = image_directory + "/test/" + drivers_df['img'][index]
    imageInfo = {}
    imageInfo['attributes'] = RekognitionInterface.recognizeLabels(filename)
    imageWrapper = []
    imageWrapper.append(drivers_df['subject'][index])
    imageInfo['subject'] = drivers_df['subject'][index]
    imageInfo['classname'] = drivers_df['classname'][index]
    imageInfo['imgname'] = drivers_df['img'][index]
    imageWrapper.append(json.dumps(imageInfo))
    print(imageWrapper)
    return imageWrapper

def makeCSV(image_directory, images_list, indexStart, indexEnd):
    drivers_df = pd.read_csv(images_list)
    with open("output2.csv", 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range (indexStart, indexEnd):
            image = getImageInfo(drivers_df, image_directory, images_list, i)
            writer.writerow(image)
        #['id'].append(image[0])
        #imagedf['attributes'].append(image[1])
    