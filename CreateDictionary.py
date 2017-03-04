import csv
import json
from pprint import pprint
def find_unique_attributes(filename):
  allUniqueAttributes = set()

  with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      #jsonStr = json.dumps(row[1])
      #jsonRow = json.loads('\"' + jsonStr + '\"')
      #jsonRow = json.loads(jsonStr)

      jsonRow = json.loads(row[1])

      for i in range(0, len(jsonRow['attributes'])):
        allUniqueAttributes.add(jsonRow['attributes'][i]['Name'])
      #data = json.loads(str(row[1]))

  return allUniqueAttributes
          
find_unique_attributes('output2.csv')

