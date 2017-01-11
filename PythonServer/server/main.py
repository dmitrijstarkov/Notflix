## TODOs
# --------------------------------------------------

# Mysql - do it according to python programming
# Dashboard the film / tv categories??
# DO the recommendations

# --------------------------------------------------

# python modules

from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL
#from MySQLdb import escape_string as thwart
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.datastructures import ImmutableOrderedMultiDict
import json, os, requests,datetime

# --------------------------------------------------

# my modules

from funcs import \
populate_cat, s, nav_links, login_required, subscription_required, populate_eps, login_attempts_numb, login_attempts_incr, usage_hist

from mysql_config import \
mysql_user, mysql_ps, mysql_db, mysql_host, mysql_port

from client_messages import \
login_error, reg_error, login_success, logout_success,\
reg_forms_error, registered_success, login_noreg_error, too_many_too_many_attempts,\
no_email_error, no_password_error


# --------------------------------------------------

# the app!

app = Flask(__name__)

# --------------------------------------------------

# MySQL configurations
# THIS IS GOING TO CHANGE!

mysql = MySQL() 
app.config['MYSQL_DATABASE_USER'] = mysql_user
app.config['MYSQL_DATABASE_PASSWORD'] = mysql_ps
app.config['MYSQL_DATABASE_DB'] = mysql_db
app.config['MYSQL_DATABASE_HOST'] = mysql_host
app.config['MYSQL_DATABASE_PORT'] = mysql_port
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

# --------------------------------------------------

# Super secret sesion key

app.secret_key=generate_password_hash(os.urandom(24))

# --------------------------------------------------

# app routes (pages etc.)

@app.route('/films',methods=['GET','POST'])
@login_required
#@subscription_required
def films_cat():
	
	# bring up the videos page for viewing
	
	if request.method == 'POST':

		usage_hist(session['user_id'],request.form['video_id'])
		
		return render_template('/videos/video.html'\
		,link=request.form['URL'],name=request.form['VIDEO TITLE']\
		,Page_Name=request.form['VIDEO TITLE']\
		,nav_links=nav_links[2:7],back='/films')
	
	# display the films catalogue	
	
	else:
		
		data=populate_cat('/movie')
		
		return render_template('/catalogue/films.html'\
		,Page_Name="Catalogue - Films"\
		,nav_links=nav_links[2:7],video_data=data)

@app.route('/tv_shows',methods=['GET','POST'])
@login_required
#@subscription_required
def tv_cat():

	# populate series page
	
	if request.method == 'GET':

		data=populate_cat('/series')
		
		return render_template('/catalogue/catalogue.html'\
		,Page_Name="Catalogue - TV Shows"\
		,nav_links=nav_links[2:7],video_data=data)

	
	# populate episodes data for carousel
	
	elif request.form['SERIES-TF'] == "True":

		title = request.form['SERIES TITLE']
		data = populate_eps('/episode/'+title)
	
		return render_template('catalogue/episode-carousel.html'\
		,name=title,Page_Name=title\
		,nav_links=nav_links[2:6],video_data=data)
	
	# bring up the videos page
	
	elif request.form['SERIES-TF'] == "False":

		title = request.form['VIDEO TITLE']
		usage_hist(session['user_id'],request.form['video_id'])
	
		return render_template('videos/video.html'\
		,link=request.form['URL'],name=title\
		,Page_Name=title,nav_links=nav_links[2:6],back='/tv_shows')

@app.route('/', methods=['GET', 'POST'])
def login():

	# what about re-routing people who haven;t got a subscription?

	error = None
	if request.method == 'POST':
		
		email,password=request.form['login-email'],request.form['login-password']
		login_tries = login_attempts_numb(email)
		
		if email \
		and password \
		and login_tries < 5:

			cursor.callproc('sp_login16',(email,password))
			mysqldata = cursor.fetchall()
			lsql = len(mysqldata)
		
			if lsql == 0:
			
				error = login_noreg_error
			
			elif lsql > 0 \
			and check_password_hash(mysqldata[0][1],password) == True:
			
				session['logged_in'] = True
			
				#cheating with subscriptions!!
			
				session['subscription'] = "Active"
				session['user_id'] = mysqldata[0][0]
				flash(login_success)
		
				return redirect(url_for('films_cat'))			

			elif lsql > 0 \
			and check_password_hash(mysqldata[0][1],password) == False :

				login_attempts_incr(email)
				error = login_error
		
		elif email \
		and password \
		and login_tries >= 5:

			login_attempts_incr(email)
			error = too_many_too_many_attempts
			
		elif not email:
			error = no_email_error
						
		elif not password:
			error = no_password_error
						
	return render_template('/users/login.html'\
	,error=error\
	,Page_Name="Login",nav_links=nav_links[1:2])

@app.route('/logout')
@login_required
def logout():

		session.pop('logged_in',None)
		flash(logout_success)
		return redirect(url_for('login'))

@app.route('/account')
@login_required
def account():
	
    return render_template('/users/account.html'\
	,Page_Name="Account Settings",nav_links=nav_links[2:7])

@app.route('/register', methods=['GET', 'POST'])
def register():

	error = None
	
	if request.method == 'POST':
		
		email,password,age =\
		 request.form['reg-email']\
		 ,request.form['reg-password']\
		 ,request.form['reg-age']
		
		if email and password and age:
			
			hashedpassword = generate_password_hash(password)
			cursor.callproc('sp_createUser3',(email,hashedpassword))

			if len(cursor.fetchall()) == 0:
				
				conn.commit()
				session['logged_in'] = True
				session['subscription']='Inactive'
				flash(s(registered_success) + s(email))
				return redirect(url_for('purchase'))
				
			else:
				error = reg_error
		else:
			error = reg_forms_error
		
	return render_template('/users/register.html',error=error\
	,Page_Name="Registration",nav_links=nav_links[0:2])

#### https://pythonprogramming.net/paypal-flask-tutorial/

@app.route('/purchase')
@login_required
def purchase():
	
	#CHEATING!
	
	session['subscription']='Inactive'
	
	return render_template('/payment/purchase.html'\
	,Page_Name="Please buy something",nav_links=nav_links[2:7])

@app.route('/ipn',methods=['POST'])
def ipn():
	arg = ''
	request.parameter_storage_class = ImmutableOrderedMultiDict
	values = request.form
	for x, y in values.iteritems():
		arg += "&{x}={y}".format(x=x,y=y)

	validate_url = 'https://www.sandbox.paypal.com' \
				   '/cgi-bin/webscr?cmd=_notify-validate{arg}' \
				   .format(arg=arg)
				   
	r = requests.get(validate_url)
	print(r.text)
	if r.text == 'VERIFIED':
		# non thwart version
		print(request.form)
		payer_email =  request.form.get('payer_email')
		unix = datetime.datetime.now()
		payment_date = request.form.get('payment_date')
		username = request.form.get('custom')
		last_name = request.form.get('last_name')
		payment_gross = request.form.get('payment_gross')
		payment_fee = request.form.get('payment_fee')
		payment_status = request.form.get('payment_status')
		txn_id = request.form.get('txn_id')
		
		# thwart version
		
		#payer_email =  thwart(request.form.get('payer_email'))
		#unix = int(time.time())
		#payment_date = thwart(request.form.get('payment_date'))
		#username = thwart(request.form.get('custom'))
		#last_name = thwart(request.form.get('last_name'))
		#payment_gross = thwart(request.form.get('payment_gross'))
		#payment_fee = thwart(request.form.get('payment_fee'))
		#payment_net = float(payment_gross) - float(payment_fee)
		#payment_status = thwart(request.form.get('payment_status'))
		#txn_id = thwart(request.form.get('txn_id'))

	return r.text


@app.route('/success')
@login_required
def success():
	
	
	# should this move to the IPN?
	# only direct users here if the subscription successed?
	# check against mysql data first?
	
	session['subscription'] = "Active"
	
	return render_template('/payment/success.html'\
	,Page_Name="Successful Payment",nav_links=nav_links[2:7])

@app.route('/payment_failed')
@login_required
def failure():
	
    return render_template('/payment/failure.html'\
	,Page_Name="Payment Failed",nav_links=nav_links[2:7])

# --------------------------------------------------

# SERVER START UP

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=82)