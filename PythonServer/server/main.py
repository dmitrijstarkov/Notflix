## TODOs
# --------------------------------------------------

# DO the recommendations

# --------------------------------------------------

# python modules

from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug import generate_password_hash, check_password_hash
from werkzeug.datastructures import ImmutableOrderedMultiDict
import json, os, datetime, time

# --------------------------------------------------

# my modules

from funcs import \
s\
, logged_in_navs\
, no_login_navs\
, login_required\
, subscription_required \
, omdb

from video_api_funcs import  populate_cat, populate_eps

from redis_funcs import\
login_hist_get\
, login_hist_add\
, count_usage\
, get_usage\
, usage_hist\
, login_attempts_numb\
, login_attempts_incr

from mysql_funcs import \
numbs_pass\
, update_password\
, get_sub_dets\
, get_all_payments\
, sub_check\
, put_sub\
, put_payment\
, ipn_validation\
, registration_check\
, login_check 

from client_messages import error_dict


# global stuff
# --------------------------------------------------

# the app!
app = Flask(__name__)

# Super secret cookie session key
app.secret_key=generate_password_hash(os.urandom(24))

# --------------------------------------------------

# app routes (pages and fucntions applied to server data etc.)

@app.route('/films',methods=['GET','POST'])
@login_required
@subscription_required
def films_cat():
	
	# bring up the videos page for viewing
	
	if request.method == 'POST':
		title = request.form['VIDEO TITLE']
		usage_hist(session['user_id'],title)
		
		return render_template('/videos/video.html'\
		,link=request.form['URL'],name=title\
		,Page_Name=title\
		,nav_links=logged_in_navs,back='/films')
	
	# display the films catalogue	
	
	else:
		
		data=populate_cat('/movie')
		
		return render_template('/catalogue/films.html'\
		,Page_Name="Catalogue - Films"\
		,nav_links=logged_in_navs,video_data=data)

@app.route('/tv_shows',methods=['GET','POST'])
@login_required
@subscription_required
def tv_cat():

	# populate series page
	
	if request.method == 'GET':

		data=populate_cat('/series')
		
		return render_template('/catalogue/catalogue.html'\
		,Page_Name="Catalogue - TV Shows"\
		,nav_links=logged_in_navs,video_data=data)
	
	# populate episodes data for carousel
	
	elif request.form['SERIES-TF'] == "True":

		title = request.form['SERIES TITLE']
		data = populate_eps('/episode/'+title)
	
		return render_template('catalogue/episode-carousel.html'\
		,name=title,Page_Name=title\
		,nav_links=logged_in_navs,video_data=data)
	
	# bring up the videos page
	
	elif request.form['SERIES-TF'] == "False":

		title = request.form['VIDEO TITLE']
		usage_hist(session['user_id'],title)
	
		return render_template('videos/video.html'\
		,link=request.form['URL'],name=title\
		,Page_Name=title,nav_links=logged_in_navs,back='/tv_shows')

@app.route('/', methods=['GET', 'POST'])
def login():


	error = None
	if request.method == 'POST':
		
		email,password=request.form['login-email'],request.form['login-password']
		login_tries = login_attempts_numb(email)
	
		if email and password and login_tries < 5:
				
			mysqldata=login_check(email,password)
			login_lsql = len(mysqldata)
		
			if login_lsql == 0:
			
				error = error_dict['login_noreg_error']
			
			elif login_lsql>0 and check_password_hash(mysqldata[0][1],password)==True:
				session['logged_in'] = True
				session['user_id'] = mysqldata[0][0]	
				lastlogin = login_hist_add(session['user_id'])
				
				flash(s(error_dict['login_success'])\
				 + ' You last logged in '+s(lastlogin))
				
				if sub_check(session['user_id']) == True:
					session['subscription'] = True
				else:
					session['subscription'] = False

				return redirect(url_for('films_cat'))			

			elif login_lsql>0 and check_password_hash(mysqldata[0][1],password)==False:

				login_attempts_incr(email)
				error = error_dict['login_error']
		
		elif email and password and login_tries >= 5:

			login_attempts_incr(email)
			error = error_dict['too_many_too_many_attempts']
		elif not email:
			error = error_dict['no_email_error']
						
		elif not password:
			error = error_dict['no_password_error']
						
	return render_template('/users/login.html'\
	,error=error\
	,Page_Name="Login",nav_links=no_login_navs)

@app.route('/logout')
@login_required
def logout():

		session.pop('logged_in',None)
		flash(error_dict['logout_success'])
		return redirect(url_for('login'))

@app.route('/account', methods=['GET', 'POST'])
@login_required
@subscription_required
def account():
	error=None
	if request.method == 'POST':
		old_pw,new1,new2,email = request.form['reg-password-old']\
		, request.form['reg-password-new1'] \
		, request.form['reg-password-new2']	\
		, request.form['reg-email']
			
		if old_pw and new1 and new2 and email:
			if new1 == new2:
				if len(new1) > 8 and numbs_pass(new1) > 2:

					mysqldata=login_check(email,old_pw)
					
					if check_password_hash(mysqldata[0][1],old_pw) == True:
					
						hashedpassword = generate_password_hash(new1)
						update_password(session['user_id'],hashedpassword)
						flash(error_dict['pass_change_success'])
						
				else:
					error =  error_dict['not_long_enough']
			else:
				error = error_dict['not_matching_passwords']
		else:
			error=error_dict['reg_forms_error']

	user = s(session['user_id'])

	payments = get_all_payments(user)	
	subs = get_sub_dets(user)
	last10 = get_usage(user)
	countvids = count_usage(user)
	loginhist=login_hist_get(user)
	
	return render_template('/users/account.html'\
	,Page_Name="Account Settings",nav_links=logged_in_navs\
	,payments=payments,subs=subs,last10=last10,countvids=countvids\
	,loginhist=loginhist)

@app.route('/register', methods=['GET', 'POST'])
def register():

	error = None
	
	if request.method == 'POST':
		
		email,password1,password2,age =\
		 str(request.form['reg-email'])\
		 ,str(request.form['reg-password1'])\
 		 ,str(request.form['reg-password2'])\
		 ,str(request.form['reg-age'])
		
		if email and password1 and password2 and age:
			if password1 == password2:
				if len(password1) > 8 and numbs_pass(password1) > 2:

					hashedpassword = generate_password_hash(password1)
					reg_check = registration_check(email,hashedpassword)
			
					if reg_check == True:
						mysqldata=login_check(email,password1)
						session['user_id'] = mysqldata[0][0]
						session['logged_in'] = True
						session['subscription'] = False
						flash(s(error_dict['registered_success']) + s(email))
						return redirect(url_for('purchase'))
				
					else:
						error = error_dict['reg_error']
				else:
					error = error_dict['not_long_enough']
			else:
				error = error_dict['not_matching_passwords']
		else:
			error = error_dict['reg_forms_error']
		
	return render_template('/users/register.html',error=error\
	,Page_Name="Registration",nav_links=no_login_navs)

@app.route('/purchase')
@login_required
def purchase():
	
	return render_template('/payment/purchase.html'\
	,Page_Name="Please buy something",nav_links=logged_in_navs)

@app.route('/ipn',methods=['POST'])
def ipn():
	
	request.parameter_storage_class = ImmutableOrderedMultiDict
	if ipn_validation(request.form) == "VERIFIED":
		now = datetime.datetime.now()
		if request.form.get('txn_type') == 'subscr_signup':
		
			sub_id = request.form.get('subscr_id')
			date = now.strftime('%Y-%m-%d %H:%M:%S')
			user_id = request.form.get('custom')
			ipn_id = request.form.get('ipn_track_id')
			paypal_email = request.form.get('payer_email')
			payer_id = request.form.get('payer_id')
		
			put_sub(sub_id,date,user_id,ipn_id,paypal_email,payer_id)
		
		elif request.form.get('txn_type') == 'subscr_payment':	

			sub_id = request.form.get('subscr_id')
			date = now.strftime('%Y-%m-%d %H:%M:%S')
			user_id = request.form.get('custom')
			ipn_id = request.form.get('ipn_track_id')
			verif_id = request.form.get('verify_sign')
			amount = request.form.get('payment_gross')
			status = request.form.get('payment_status')
			txn_id = request.form.get('txn_id')
		
			put_payment(sub_id,date,user_id,ipn_id,verif_id,amount,status,txn_id)

	return 'hello'

@app.route('/success')
@login_required
def success():
	
	session['subscription'] = True
	
	return render_template('/payment/success.html'\
	,Page_Name="Successful Payment",nav_links=logged_in_navs)

@app.route('/payment_failed')
@login_required
def failure():
	
    return render_template('/payment/failure.html'\
	,Page_Name="Payment Failed",nav_links=logged_in_navs)

# --------------------------------------------------

# SERVER START UP

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=80)