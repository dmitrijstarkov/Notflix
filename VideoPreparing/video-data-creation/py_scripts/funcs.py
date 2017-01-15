#funcs.py
from video_api import login
import requests, hashlib, os

pathtodo = '/todo_python/'
pathtoput = '/encoded_video/'

def metadata(string,path):

	newstring = "".join(open(path+string+'/metadata.txt','r').readlines())
	print('+++++ Directory: '+string+' ++ ID: '+s(newstring))

	return newstring

def s(string):
	
	value = str(string)
	return value

def dbstatus(string):

	dbstatus = requests.get(string,data=None,auth=login)
	if dbstatus.status_code == 404:
		print("DB gave a 404 response...\nA new DB will created for:"+string)
		if make_db.status_code == 201:
			print("+++",make_db.status_code,string,"DB created")			
		else:
			print('+++',make_db.status_code,string,"DB not created")

def collection_check(string):

	coll = get(string)
	if coll.status_code == 404:
		
		print(string + "\nGave a 404 response. Adding.")
		make_series_coll = put_place(string)

def omdb(string):
	
	vid_meta = requests.get(\
	"http://www.omdbapi.com/?i="+string+"&plot=short&r=json",params=None).json()
	return vid_meta

def db_post(string,json_data):

	postvalue = requests.post(string,json=json_data,auth=login)
	print(string+' metadata POST: ' + s(postvalue.status_code))

def get(place):
	
	getvalue = requests.get(place,data=None,auth=login)
	return getvalue

def put_place(place):
	
	putvalue = requests.put(place,data=None,auth=login)
	print('PUT to '+place+': '+s(putvalue.status_code))

def delete(place):
	
	deleting = requests.delete(place,data=None,auth=login)
	print(place+' db deleted')

def hashing(string,path):
	rename=hashlib.md5(str(string)).hexdigest()
	os.rename(path+string,path+rename)
	print(s(string) + ' renamed to: ' + s(rename))
	print('--------------------')
	
	return rename
	