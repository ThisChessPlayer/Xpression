import csv
import json
from pprint import pprint
import CreateDictionary
'''
def find_confidence_attributes(filename):

  allUniqueAttributes = []
  with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      #jsonStr = json.dumps(row[1])
      #jsonRow = json.loads('\"' + jsonStr + '\"')
      #jsonRow = json.loads(jsonStr)

      jsonRow = json.loads(row[1])
      #jsonRow['imgname']
      
      for i in range(0, len(jsonRow['attributes'])):
        if jsonRow['attributes'][i]['Name']
        allUniqueAttributes.append(jsonRow['attributes'][i]['Confidence'])
      #data = json.loads(str(row[1]))
      

  return allUniqueAttributes
'''

def write_to_csv(inputFile, outputFile):
  with open(outputFile, 'w', newline='') as output:

    writer = csv.writer(output)
    listOfAttribute = list(CreateDictionary.find_unique_attributes(inputFile))
    listOfAttribute.insert(0, 'img')
    listOfAttribute.insert(0, 'subject')
    listOfAttribute.insert(0, 'classname')
    writer.writerow(listOfAttribute)
    with open(inputFile) as csvfile:
      csvreader = csv.reader(csvfile)

      for row in csvreader:
        jsonRow = json.loads(row[1])
        imageattributes = [0] *len(listOfAttribute)
        imageattributes[0] = jsonRow['classname']
        imageattributes[1] = jsonRow['subject']
        imageattributes[2] = jsonRow['imgname']
        
        for i in range(0, len(jsonRow['attributes'])):
          imageattributes[listOfAttribute.index(jsonRow['attributes'][i]['Name'])]=jsonRow['attributes'][i]['Confidence']
        writer.writerow(imageattributes)

def write_test_to_csv(inputFile, outputFile):
  with open(outputFile, 'w', newline='') as output:

    writer = csv.writer(output)
    listOfAttribute = list(CreateDictionary.find_unique_attributes(inputFile))
    listOfAttribute.insert(0, 'img')
    listOfAttribute.insert(0, 'subject')
    writer.writerow(listOfAttribute)
    with open(inputFile) as csvfile:
      csvreader = csv.reader(csvfile)

      for row in csvreader:
        jsonRow = json.loads(row[1])
        imageattributes = [0] *len(listOfAttribute)
        imageattributes[0] = jsonRow['subject']
        imageattributes[1] = jsonRow['imgname']
        
        for i in range(0, len(jsonRow['attributes'])):
          imageattributes[listOfAttribute.index(jsonRow['attributes'][i]['Name'])]=jsonRow['attributes'][i]['Confidence']
        writer.writerow(imageattributes)


#write_to_csv('drivers.csv', 'labeledfeatures.csv')

#write_test_to_csv('test_preprocess_output.csv', 'test_features.csv')