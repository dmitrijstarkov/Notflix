import json
from funcs import s
from restheart import \
post_resource, get_resource, put_resource, get_omdb
from video_api import _BASE_URL


def populate_cat(string):

	metadata=get_resource(_BASE_URL+string,params=None).json()['_embedded']['rh:coll']
	trans_list=[metadata[i]['_id'] for i,j in enumerate(metadata)]

	page_metadata=\
	{i:[get_resource(_BASE_URL+string+'/'+s(i),params=None).json()\
	['_embedded']['rh:doc'][0]] for i in trans_list}
	
	return page_metadata

def populate_eps(string):

	data=get_resource(_BASE_URL+string,params=None).json()['_embedded']['rh:doc']
	
	return data