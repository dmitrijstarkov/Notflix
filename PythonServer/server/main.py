## TODOs
# --------------------------------------------------

# DO the recommendations

# --------------------------------------------------

# python modules

from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.datastructures import ImmutableOrderedMultiDict
import json, os, requests, datetime

# --------------------------------------------------

# my modules

from funcs import \
populate_cat, s, nav_links, login_required, subscription_required \
, populate_eps, login_attempts_numb, login_attempts_incr, usage_hist \
, login_check, registration_check, ipn_validation, put_payment, put_sub


from client_messages import \
login_error, reg_error, login_success, logout_success\
, reg_forms_error, registered_success, login_noreg_error\
, too_many_too_many_attempts, no_email_error, no_password_error

# --------------------------------------------------

# the app!

app = Flask(__name__)

# --------------------------------------------------

# Super secret sesion key

app.secret_key=generate_password_hash(os.urandom(24))

# --------------------------------------------------

# app routes (pages and fucntions applied to server data etc.)

@app.route('/films',methods=['GET','POST'])
#@login_required
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
#@login_required
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
				
			mysqldata=login_check(email,password)
			login_lsql = len(mysqldata)
		
			if login_lsql == 0:
			
				error = login_noreg_error
			
			elif login_lsql > 0 \
			and check_password_hash(mysqldata[0][1],password) == True:
			
				session['logged_in'] = True
			
				#cheating with subscriptions!!
			
				session['subscription'] = "Active"
				session['user_id'] = mysqldata[0][0]
				flash(login_success)
		
				return redirect(url_for('films_cat'))			

			elif login_lsql > 0 \
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
		 str(request.form['reg-email'])\
		 ,str(request.form['reg-password'])\
		 ,str(request.form['reg-age'])
		
		if email and password and age:
			
			hashedpassword = generate_password_hash(password)
			reg_check = registration_check(email,hashedpassword)
			
			if reg_check == True:
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
	
	#arg = ''
	request.parameter_storage_class = ImmutableOrderedMultiDict
	#values = request.form


	#for x, y in values.iteritems():
	#	arg += "&{x}={y}".format(x=x,y=y)
	#
	#validate_url = 'https://www.sandbox.paypal.com' \
	#			   '/cgi-bin/webscr?cmd=_notify-validate{arg}' \
	#			   .format(arg=arg)
				   
	#r = requests.get(validate_url)

	#print(r.text)
	
	ipn_validation(request.form)
	
	if request.form.get('txn_type') == 'subscr_signup':
		
		print('putting stuff to the subscriptions db')
		
		sub_id = request.form.get('subscr_id')
		date = datetime.datetime.now()
		user_id = request.form.get('custom')
		ipn_id = request.form.get('ipn_track_id')
		paypal_email = request.form.get('payer_email')
		payer_id = request.form.get('payer_id')
		
		#cursor.callproc('sp_createUser3',(email,hashedpassword))
		
		put_payment(\
		sub_id\
		,date\
		,user_id\
		,ipn_id\
		,paypal_email\
		,payer_id)
		
	elif request.form.get('txn_type') == 'subscr_payment':
		
		print('put stuff to the payments db')	

		sub_id = request.form.get('subscr_id')
		date = datetime.datetime.now()
		user_id = request.form.get('custom')
		ipn_id = request.form.get('ipn_track_id')
		verif_id = request.form.get('verify_sign')
		amount = request.form.get('payment_gross')
		status = request.form.get('payment_status')
		txn_id = request.form.get('txn_id')
		#cursor.callproc('sp_createUser3',(email,hashedpassword))
		
		put_sub(\
		sub_id\
		,date\
		,user_id\
		,ipn_id \
		,verif_id\
		,amount\
		,status\
		,txn_id)

	return 'hello'

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