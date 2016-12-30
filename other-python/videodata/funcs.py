#funcs.py

import requests
import hashlib
import os

def metadata(string):

	newstring = "".join(open(string+'/metadata.txt','r').readlines())
	print('+++++ Directory: '+string+' ++ ID: '+s(newstring))

	return newstring

def s(string):
	
	value = str(string)
	return value

def dbstatus(string):

	dbstatus = requests.get(string,data=None,auth=('admin','changeit'))
	if dbstatus.status_code == 404:
		print("DB gave a 404 response...\nA new DB will created for:"+string)
		if make_db.status_code == 201:
			print("+++",make_db.status_code,string,"DB created")			
		else:
			print('+++',make_db.status_code,string,"DB not created")

	
def omdb(string):
	
	vid_meta = requests.get(\
	"http://www.omdbapi.com/?i="+string+"&plot=short&r=json",params=None).json()
	return vid_meta

def db_post(string,json_data):

	postvalue = requests.post(string,json=json_data,auth=('admin','changeit'))
	print(string+' metadata POST: ' + s(postvalue.status_code))

def get(place):
	
	getvalue = requests.get(place,data=None,auth=('admin','changeit'))
	
	return getvalue

def put_place(place):
	
	putvalue = requests.put(place,data=None,auth=('admin','changeit'))
	print('PUT to '+place+': '+s(putvalue.status_code))

def delete(place):
	
	deleting = requests.delete(place,data=None,auth=('admin','changeit'))
	print(place+' db deleted')

def hashing(string):
	
	rename=hashlib.md5(str(string)).hexdigest()
	os.rename(string,rename)
	print(s(string) + ' renamed to: ' + s(rename))
	print('--------------------')