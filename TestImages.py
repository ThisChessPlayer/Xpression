import utility
import CreateImageFeatures
import csv

import os
try:
  import pyodbc
except ImportError:
  import odbc as pyodbc

def format_sql_request(headerFileName, imageDataFileName):
  with open(headerFileName, 'r') as headerFile:
    headerReader = csv.reader(headerFile)
    with open(imageDataFileName, 'r') as imageDataFile:
      imageDataReader = csv.reader(imageDataFile)
      for j in headerReader:
        header = j
      imageData = []
      
      imageDataHeader = imageDataReader.__next__()
      imageData.append(header)
      for row in imageDataReader:
        imageInfo = [0] * len(header)
        for i in range(len(row)):
          if imageDataHeader[i] in header:
            imageInfo[header.index(imageDataHeader[i])] = row[i]
        imageData.append(imageInfo)
      #print(imageData)
      #with open("sqlPair.csv", 'w', newline='') as pairoutput:
      #  writer = csv.writer(pairoutput)
      #  for row in imageData:
      #    writer.writerow(row)
      #conn = pyodbc.connect('DRIVER={Teradata Database ODBC Driver 16.00};DSN=asterqueen.teradatalabs.net;UID=hack10user;PASSWORD=Clymene64982')
      '''
      conn = pyodbc.connect('DRIVER={Aster ODBC Driver};SERVER=asterqueen.teradatalabs.net;PORT=2406;DATABASE=hackathon.image_inputs;UID=hack10user;PWD=Clymene64982')

      cursor = conn.cursor()

      for r in imageData:
        cursor.execute("""insert into public.test3 values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", r)

      cursor.commit()
      '''
utility.makeTestCSV('imgs')
CreateImageFeatures.write_test_to_csv('test_preprocess_output.csv', 'test_features.csv')
format_sql_request("header.csv", "test_features.csv")