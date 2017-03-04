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
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint(response)
  return response

def pushJSONToTDB(json, username, password, dbAlias):
  url = 'http://teradata-rest.teradatalabs.net:1080/tdrest/systems/' +dbAlias + '/queries'
  # Setup required HTTP headers
  headers={}
  headers['Content-Type'] = 'application/json'
  headers['Accept'] = 'application/vnd.com.teradata.rest-v1.0+json'
  headers['Authorization'] = "Basic %s" % base64.encodestring('%s:%s' % (username, password)).replace('\n', ''); 

  # Uncomment to receive results gzip compressed.
  #headers['Accept-Encoding'] = 'gzip'

  # Set query bands
  queryBands = {}
  queryBands['applicationName'] = 'XPression'
  queryBands['version'] = '1.0'

  # Set request fields, including SQL.
  data = {}
  data['query'] = 'SELECT * FROM DBC.DBCInfo'
  data['queryBands'] = queryBands
  data['format'] = 'array'

  # Build request.
  request = urllib2.Request(url, json.dumps(data), headers)

  #Submit request
  try:
  response = urllib2.urlopen(request)
  # Check if result have been compressed.
  if response.info().get('Content-Encoding') == 'gzip':  
    response = zlib.decompress(response.read(), 16+zlib.MAX_WBITS)    
  else:
    response = response.read()
  except urllib2.HTTPError, e:
    print 'HTTPError = ' + str(e.code)
    response = e.read();
  except urllib2.URLError, e:
    print 'URLError = ' + str(e.reason)
    response = e.read();

  # Parse response to confirm value JSON.
  results = json.loads(response)

  return results

pp = pprint.PrettyPrinter(indent=4)

r1 = recognizeImage('test3.jpg')
pp.pprint(r1)

