import MySQLdb, requests, datetime, json, os
from funcs import s
from mysql_config import connect_mysql, login_conn, pay_conn, sub_conn

def login_check(str1,str2):

	logins_db = connect_mysql(login_conn)
	logins_cursor = logins_db.cursor()
	
	logins_cursor.callproc('sp_login16',(str1,str2))
	data = logins_cursor.fetchall()
	logins_db.close()
	
	return data
	
def registration_check(str1,str2):

	logins_db = connect_mysql(login_conn)
	logins_cursor = logins_db.cursor()
		
	logins_cursor.callproc('sp_createUser3',(str1,str2))
	data = len(logins_cursor.fetchall())
	
	if data == 0:
		logins_db.commit()
		logins_db.close()
		return True
	
	else:
		logins_db.close()
		return False
	
def ipn_validation(input1):
	
	arg = ''
	
	for x, y in input1.iteritems():
		arg += "&{x}={y}".format(x=x,y=y)

	validate_url = 'https://www.sandbox.paypal.com' \
				   '/cgi-bin/webscr?cmd=_notify-validate{arg}' \
				   .format(arg=arg)
				   
	r = requests.get(validate_url)
	
	return r.text

def put_payment(in1,in2,in3,in4,in5,in6,in7,in8):
	
	payments_db = connect_mysql(pay_conn)
	payments_cursor = payments_db.cursor()	
	payments_cursor.callproc('sp_createPayment',(in1,in2,in3,in4,in5,in6,in7,in8))
	payments_db.commit()
	payments_db.close()
		
def put_sub(in1,in2,in3,in4,in5,in6):
	
	subs_db = connect_mysql(sub_conn)
	subs_cursor = subs_db.cursor()
	subs_cursor.callproc('sp_createSub',(in1,in2,in3,in4,in5,in6))
	subs_db.commit()
	subs_db.close()	

def sub_check(in1):
	
	subs_db = connect_mysql(sub_conn)
	subs_cursor = subs_db.cursor()	
	subs_cursor.callproc('sp_checkSub',(s(in1)))
	data = len(subs_cursor.fetchall())
	subs_db.close()
	if data == 0:
		return False
	else:
		return True

def get_all_payments(in1):
	
	payments_db = connect_mysql(pay_conn)
	payments_cursor = payments_db.cursor()
	payments_cursor.callproc('sp_getPayments',s(in1))
	data = payments_cursor.fetchall()
	payments_db.close()
	return data

def get_sub_dets(in1):
	
	subs_db = connect_mysql(sub_conn)
	subs_cursor = subs_db.cursor()
	subs_cursor.callproc('sp_getSub',s(in1))
	data = subs_cursor.fetchone()
	subs_db.close()
	return data

def update_password(in1,in2):
	
	logins_db = connect_mysql(login_conn)
	logins_cursor = logins_db.cursor()
	logins_cursor.callproc('sp_updatePassword',(in1,in2))
	logins_db.commit()
	logins_db.close()
	
def numbs_pass(str1):
	counter = 0
	numbers = [s(i) for i in range(0,9)]
	for i in str1:
		if i not in numbers:
			continue
		else:
			counter += 1
	return counter