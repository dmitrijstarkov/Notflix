from restheart import \
post_resource, get_resource, put_resource, get_omdb
import json
from video_api import \
_BASE_URL

def s(string):
	
	s=str(string)
	
	return s

def unique(seq):

	# not order preserving
	set = {}
	map(set.__setitem__, seq, [])
	return set.keys()

def populate_cat(string):
		
	metadata=get_resource(_BASE_URL+string,params=None).json()['_embedded']['rh:coll']

	trans_list=[metadata[i]['_id'] for i,j in enumerate(metadata)]

	page_metadata=\
	{i:[get_resource(_BASE_URL+string+'/'+s(i),params=None).json()\
	['_embedded']['rh:doc'][0]] for i in trans_list}
	
	if string == '/episode':
	
		return page_metadata, trans_list
		
	else:
		
		return page_metadata