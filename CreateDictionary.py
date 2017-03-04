import csv
import json
def find_unique_attributes(filename):
  with open(filename) as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
      jsonRow = json.loads("\"" + row[1] + "\"")
      print(jsonRow[0])
      
      #data = json.loads(str(row[1]))
          
find_unique_attributes('output.csv')

