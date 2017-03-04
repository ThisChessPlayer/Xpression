import csv
import json
import teradata
import boto3 as b3
import pandas as pd
import sys
import RekognitionInterface
import os
import boto3
import pprint

udaExec = teradata.UdaExec(appName= "hackathon", version = 1, logConsole = True)
con = udaExec.connect(method = "odbc", system = "tdmpp01cop1.teradatalabs.net", username = "hack10user", password = "Clymene64982")
cursor = con.cursor()
sql = """insert into hack10.image_results (driver_license, image_results) values (?, ?)"""
img_list = "/qd0047/tl151006/hack/img/driver_imgs_list.csv"
image_directory = "/qd0047/tl151006/hack/img"
drivers_df = pd.read_csv(img_list)

def getImageInfo(drivers_df, image_directory, images_list, index):

    drivers_list = []

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
    json.dumps(imageInfo)
    imageWrapper.append(json.dumps(imageInfo))
    print(imageWrapper)
    return imageWrapper
    
if __name__ == "__main__":
    try:
        i = 0
        while i < 22423:
            row = getImageInfo(drivers_df, image_directory, img_list, i)
            i += 1
            cursor.execute (sql, row)

    except Exception as e:
        raise
