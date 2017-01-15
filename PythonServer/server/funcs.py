import json, datetime, requests, os
from functools import wraps
from flask import session, flash, redirect, url_for

from restheart import \
post_resource, get_resource, put_resource, get_omdb

from video_api import _BASE_URL
from client_messages import error_dict

logged_in_navs={\
"LOGOUT":"/logout" \
,"TV SHOWS":"/tv_shows" \
,"FILMS":"/films" \
,"ACCOUNT":"/account"}

no_login_navs={\
"LOGIN":"/" \
,"REGISTER":"/register" }


# wrappers ---------------------

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash(error_dict['no_session'])
			return redirect(url_for('login'))
	return wrap

def subscription_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):

		if 'subscription' in session:
			return f(*args,**kwargs)
		else:
			flash(error_dict['no_subscription'])
			return redirect(url_for('purchase'))
	return wrap

# Misc -------------------------

def omdb(string):
	
	vid_meta = requests.get(\
	"http://www.omdbapi.com/?i="+string+"&plot=short&r=json",params=None).json()
	return vid_meta

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
	
	return page_metadata

def populate_eps(string):

	data=get_resource(_BASE_URL+string,params=None).json()['_embedded']['rh:doc']
	
	return data