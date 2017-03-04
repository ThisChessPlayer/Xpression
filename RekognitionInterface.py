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

  return response

#response = recognizeFaces('imgs/test/img_1.jpg')
#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(response)