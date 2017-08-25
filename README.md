--------------------------------------------------------------------------------
             _   _ _____ _____ _____ _____ _____ _____ _____ _____              
            \ \ / /  _  |  _  \  ___|  ___|  ___|_   _|  _  |  _  |             
             \ v /| |_| | |_| / |___| |___| |___  | | | | | | | | |             
              | | |  ___|  _  \  ___|___  |___  | | | | | | | | | |             
             / ^ \| |   | | | | |___ ___| |___| |_| |_| |_| | | | |             
            /_/ \_\_|   |_| |_|_____|_____|_____|_____|_____|_| |_|             
--------------------------------------------------------------------------------
Machine Learning application using AWS Rekognition and Teradata Aster used to classify drivers into one of ten categories, each representing different levels of distraction. Edit
Add topics
--------------------------------------------------------------------------------
Dependencies:
  - AWSCLI
    - Access to AWS Rekognition
  - Teradata Services
    - Access to Teradata Aster
    - Access to TDBMS
--------------------------------------------------------------------------------
Program Overview:
  There are several portions of the pipeline that need to be run in order to
  preprocess data, store it, and then operate on it using Aster. 

  1. Preprocessing
  - Ensure AWSCLI is set
    up with the proper credentials.
  - Run utility.py's functions as appropriate. It uses RekognitionInterface's 
    definitions to use pass images through AWS Rekognition. The returned
    results can be placed in a CSV file for easy importing into a Teradata
    database.

  2. Storing data
  - Once the database is set up, run TestImages.py to place the data into the
    database using a SQL query.

  3. Using Aster
  - Use the SVM function on the imported data to classify image features.
--------------------------------------------------------------------------------

