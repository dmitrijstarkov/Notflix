import json, redis, datetime
from functools import wraps
from flask import session, flash, redirect, url_for

from restheart import \
post_resource, get_resource, put_resource, get_omdb

from video_api import _BASE_URL

r_login_attempts = redis.Redis(host='172.17.0.6',port='6379')
r_usage = redis.Redis(host='172.17.0.9',port='6379')

nav_links=["/"\
,"/register"\
,"/logout"\
,"/tv_shows"\
,"/films"\
,"/account"\
,"/purchase"]

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
				flash('Please login first')
				return redirect(url_for('login'))
	return wrap

def subscription_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		
		if session['subscription'] == "Inactive":
			return f(*args,**kwargs)
		else:
				flash('Please set up a subscription first.')
				return redirect(url_for('purchase'))
	return wrap
	
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

def login_attempts_incr(string):
	
	r_login_attempts.lpush(string,datetime.datetime.now())
	r_login_attempts.expire(string,60)
	
def login_attempts_numb(string):
	
	attempts_int = r_login_attempts.llen(string)
	
	return attempts_int
	
def usage_hist(str1,str2):
	
	r_usage.lpush(str1,str2)