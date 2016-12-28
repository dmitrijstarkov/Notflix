from flask import \
Flask, render_template, redirect, url_for, request, session, flash

from functools import \
wraps

from restheart import \
post_resource, get_resource, put_resource, get_omdb

from video_api import \
_BASE_URL

from funcs import unique

import json

nav_links=["/"\
,"/register"\
,"/logout"\
,"/tv_shows"\
,"/films"\
,"/account"]

# create the application object
app = Flask(__name__)

# use a random key generator (form seperate config file)
app.secret_key= "my precious" 


def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
				flash('Please login first')
				return redirect(url_for('login'))
	return wrap

@app.route('/films',methods=['GET','POST'])
@login_required
def films_cat():
	
	if request.method == 'POST':
	
		# todo PUT to usage database
	
		print(request.form['URL'])
		return render_template(\
		'/videos/video.html'\
		,link=request.form['URL']\
		,name=request.form['VIDEO TITLE']\
		,Page_Name=request.form['VIDEO TITLE']\
		,nav_links=nav_links[2:6]\
		,back='/films')
	
	else:
		
		payloadmovie=get_resource(_BASE_URL+'/movie',params=None).json()
		movie_json=payloadmovie['_embedded']['rh:coll']
		
		filmlist=[movie_json[i]['_id'] for i,j in enumerate(movie_json)]
		
		film_metadata={i:[get_resource(_BASE_URL+'/movie/'+str(i),params=None)\
		.json()['_embedded']['rh:doc'][0]] for i in filmlist}
		
		return render_template(\
		'/catalogue/films.html'\
		,video_data=film_metadata\
		,Page_Name="Catalogue - Films"\
		,nav_links=nav_links[2:6])


# use decorators to link the function to a url
@app.route('/tv_shows',methods=['GET','POST'])
@login_required
def tv_cat():
	
	if request.method == 'POST':

		# todo PUT to usage database

		print(request.form['URL'])
		return render_template(\
		'videos/video.html'\
		,link=request.form['URL']\
		,name=request.form['VIDEO TITLE']\
		,Page_Name=request.form['VIDEO TITLE']\
		,nav_links=nav_links[2:6]\
		,back='/tv_shows')
	
	else:

		# this is only brining back video data for one series title
		# does the put in mondodb_data.py need to be changed?

		series_metadata=get_resource(\
		_BASE_URL+'/episode'\
		,params=None).json()

		hello=series_metadata['_embedded']['rh:coll']
		tv_list=[hello[i]['_id'] for i,j in enumerate(hello)]

		tv_metadata={i:[get_resource(_BASE_URL+'/episode/'+str(i)\
		,params=None).json()['_embedded']['rh:doc'][0]] for i in tv_list}
		
		return render_template(\
		'/catalogue/catalogue.html'\
		,series=tv_list\
		,video_data=tv_metadata\
		,Page_Name="Catalogue - TV Shows"\
		,nav_links=nav_links[2:6])

# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
	
	error = None
	if request.method == 'POST':

		if request.form['username'] != 'admin' \
		or request.form['password'] != 'admin':
		
			error = 'Invalid Credentials. Please try again.'
			
		else:
			
			session['logged_in'] = True
			flash('You have been logged in')
			return redirect(url_for('catalogue'))
			
	return render_template('/users/login.html'\
	,error=error\
	,Page_Name="Login"\
	,nav_links=nav_links[1:2])


@app.route('/logout')
@login_required
def logout():

		session.pop('logged_in',None)
		flash('You have been logged out')
		return redirect(url_for('login'))


# route for handling the registration
@app.route('/register', methods=['GET', 'POST'])
def register():

    error = None
    if request.method == 'POST':
		
        if request.form['username'] != 'admin' \
		or request.form['password'] != 'admin':
		
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('login'))
    
	return render_template(\
	'/users/register.html'\
	,error=error\
	,Page_Name="Registration"\
	,nav_links=nav_links[0:2])

@app.route('/account')
@login_required
def account():
	
    return render_template(\
	'/users/account.html'\
	,Page_Name="Account Settings"\
	,nav_links=nav_links[2:5])  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=82)
