import redis, datetime, json, os

from funcs import s

r_login_attempts = redis.Redis(host='login-attempts',port='6379')
r_login_hist = redis.Redis(host='login-history',port='6379')
r_usage = redis.Redis(host='usage-db',port='6379')

def login_attempts_incr(in1):
	
	r_login_attempts.lpush(in1,datetime.datetime.now())
	r_login_attempts.expire(in1,60)
	
def login_attempts_numb(in1):
	
	return r_login_attempts.llen(in1)
	
def usage_hist(in1,in2):
	
	r_usage.lpush(in1,in2)

def get_usage(in1):
	
	if r_usage.llen(in1) == 0:
		return None
	else:
		return r_usage.lrange(in1,0,10)
		
def count_usage(in1):
	
	if r_usage.llen(in1) == 0:
		return None
	else:
		data = r_usage.lrange(in1,0,r_usage.llen(in1))
		newdict={}
		for i in data:
			if i not in newdict:
				newdict[i]=0
			newdict[i]+=1
		
		return newdict

def login_hist_add(in1):
	
	r_login_hist.lpush(in1,datetime.datetime.now())
	data = r_login_hist.lrange(in1,0,0)
	return data[0].split('.')[0]

def login_hist_get(in1):

	data = [i.split('.')[0] for i in r_login_hist.lrange(in1,0,10)]
	return data
