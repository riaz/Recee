import json
import requests
import urllib2

"""
data_json = json.dumps(data)
r = requests.get('http://localhost:5000/post/', data=data_json)

"""
url = "http://localhost:3000"
#req = urllib2.Request('')

payload = {'lat':37.4419, 'lng' : -122.1419, 'path': '/home/riaz/Desktop/Recce/datasets/I1_000000.png'}
headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers)
print response
