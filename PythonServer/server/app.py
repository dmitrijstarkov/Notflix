# import the Flask class from the flask module
from flask import Flask, render_template, redirect, \
	url_for, request, session, flash
from functools import wraps
from restheart import post_resource, get_resource, put_resource
from video_api import VIDEO_DATABASE_URL, VIDEO_COLLECTION_URL, VIDEO_HEADERS
import json

nav_links=["/"\
,"/register"\
,"/logout"\
,"/videos"\
,"/account"]

nav_names=["| Login"\
,"| Register"\
,"| Logout"\
,"| Video Collection"\
,"| Account Settings"]


dict_nav = {nav_links[i] : nav_names[i] for i in range(0,len(nav_links))}
print(dict_nav)

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
		
		r=request.form['video_url']
		
		return render_template('/videos/video.html'\
		,link="http://localhost:81/"+ r +"/manifest.mpd"\
		,name=request.form['video_name']\
		,Page_Name=request.form['video_name']\
		,nav_links=nav_links[2:5])
	
	else:
		payload=get_resource(VIDEO_COLLECTION_URL,params=None).json()
		dvids = {i['video_name']:[i['video_url']\
		,i['video_genre']\
		,i['video_title']\
		,i['video_description']] for i in payload['_embedded']['rh:doc']}
		
		
		return render_template('/catalogue/catalogue.html'\
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
    return render_template('/users/register.html'\
	,error=error\
	,Page_Name="Registration"\
	,nav_links=nav_links[0:2])

@app.route('/account')
@login_required
def account():
    return render_template('/users/account.html'\
	,Page_Name="Account Settings"\
		,nav_links=nav_links[2:5])  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
