import boto3 as b3
import pandas as pd
import sys
import RekognitionInterface
import os
import csv
import json
import pprint

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

def makeCSV(indexStart, indexEnd, image_directory=".", images_list="driver_imgs_list.csv"):
    drivers_df = pd.read_csv(images_list)
    with open("output14.csv", 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range (indexStart, indexEnd):
            image = getImageInfo(drivers_df, image_directory, images_list, i)
            writer.writerow(image)
        #['id'].append(image[0])
        #imagedf['attributes'].append(image[1])

def getTestImageInfo(drivers_df, image_directory, images_list, index):

    #drivers_df = pd.read_csv(images_list)

    filename = image_directory + "/test/" + drivers_df['img'][index]
    print('Image: ' + filename)
    imageInfo = {}
    imageInfo['attributes'] = RekognitionInterface.recognizeLabels(filename)
    imageWrapper = []
    imageWrapper.append(drivers_df['subject'][index])
    imageInfo['subject'] = drivers_df['subject'][index]
    imageInfo['imgname'] = drivers_df['img'][index]
    imageWrapper.append(json.dumps(imageInfo))
    return imageWrapper
    
def makeTestCSV(image_directory=".", images_list="test_imgs_list.csv"):
    drivers_df = pd.read_csv(images_list)
    with open("test_preprocess_output.csv", 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for i in range (len(drivers_df['subject'])):
            image = getTestImageInfo(drivers_df, image_directory, images_list, i)
            writer.writerow(image)
        #['id'].append(image[0])
        #imagedf['attributes'].append(image[1])

#makeTestCSV('imgs')