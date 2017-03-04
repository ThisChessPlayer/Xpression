import boto3
import pprint
import urllib


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
  #pp = pprint.PrettyPrinter(indent=4)
  #pp.pprint(response)
  return response

pp = pprint.PrettyPrinter(indent=4)

r1 = recognizeImage('test3.jpg')
pp.pprint(r1)
