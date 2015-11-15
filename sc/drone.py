import requests
import json
dictToSend = {'question':'what is the answer?'}
res = requests.post('http://localhost:5000/tests/endpoint', data=json.dumps(dictToSend))
print 'response from server:',res.text
