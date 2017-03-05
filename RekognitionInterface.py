import boto3
import pprint

def recognizeLabels(image_path):
  client = boto3.client('rekognition')

  # Our source image: http://i.imgur.com/OK8aDRq.jpg
  with open(image_path, 'rb') as source_image:
      source_bytes = source_image.read()

  response = client.detect_labels(
      Image={
          'Bytes': source_bytes,
      },
      MaxLabels=123
  )
  pprint.pprint(response['Labels'], indent=4)

  return response['Labels']

def recognizeFaces(image_path):
  client = boto3.client('rekognition')

  # Our source image: http://i.imgur.com/OK8aDRq.jpg
  with open(image_path, 'rb') as source_image:
      source_bytes = source_image.read()

  response = client.detect_faces(
      Image={
          'Bytes': source_bytes,
      },
      Attributes=['ALL']
  )

  response['ResponseMetadata'] = None

  if(response['FaceDetails'] != []):
    response['FaceDetails'][0]['Landmarks'] = None
  else:
    response = None

  return response
'''
pp = pprint.PrettyPrinter(indent=4)

response = recognizeFaces('makeup2.jpg')
pp.pprint(response)

response = recognizeLabels('makeup.jpg')
pp.pprint(response)
'''