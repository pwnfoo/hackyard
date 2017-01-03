#!/usr/bin/env python

from requests import session
import urllib2,json

def makepayload():
	payload={}
	payload['target_url']=raw_input("URL : ")
	return dict(payload)

def makejson():
	return json.dumps(makepayload())

with session() as c:
    response=c.post('http://127.0.0.1:8009/api/targets/', data=json.loads(makejson()))
    #print(response.headers)
    print(response.text)


