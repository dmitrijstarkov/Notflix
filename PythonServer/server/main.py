from flask import \
Flask, render_template, redirect, url_for, request, session, flash

from functools import \
wraps

from restheart import \
post_resource, get_resource, put_resource, get_omdb

from video_api import \
EP_COLLECTION_URL, FILM_COLLECTION_URL

import json

nav_links=["/"\
,"/register"\
,"/logout"\
,"/videos"\
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



# use decorators to link the function to a url
@app.route('/videos',methods=['GET','POST'])
@login_required
def catalogue():
	
	if request.method == 'POST':
		print(request.form['URL'])
		return render_template(\
		'/videos/video.html'\
		,link=request.form['URL']\
		,name=request.form['VIDEO TITLE']\
		,Page_Name=request.form['VIDEO TITLE']\
		,nav_links=nav_links[2:5])
	
	else:
		payloadtv=get_resource(\
		EP_COLLECTION_URL\
		,params=None).json()
		
		payloadmovie=get_resource(\
		FILM_COLLECTION_URL\
		,params=None).json()
		 
		#print(payloadtv)
		
		dvids = {\
		i['Title']\
		:[i['server_url']\
		,i['Series Title']\
		,i['Genre']\
		,i['Plot']\
		,i['Season']\
		,i['Episode']\
		,i['Runtime']\
		,i['imdbRating']\
		] for i in payloadtv['_embedded']['rh:doc']}
		
		return render_template(\
		'/catalogue/catalogue.html'\
		,video_data=dvids\
		,Page_Name="Catalogue"\
		,nav_links=nav_links[2:5])

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
