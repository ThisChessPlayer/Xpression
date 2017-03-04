import boto3
import pprint

def recognizeImage(image_url):
  client = boto3.client('rekognition')

  # Our source image: http://i.imgur.com/OK8aDRq.jpg
  with open(image_url, 'rb') as source_image:
      source_bytes = source_image.read()

  response = client.detect_labels(
      Image={
          'Bytes': source_bytes,
      },
      MaxLabels=123
  )

  return response['Labels']