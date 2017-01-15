import MySQLdb

login_conn = ["logins-db","logins","w44tldsg4","logins_db"]
pay_conn = ["payment-db","pay","385dgh439","payment_db"]
sub_conn = ["subscription-db","subs","this15anew_paw04d","subscription_db"]


def connect_mysql(connlist):
	
	conn = MySQLdb.connect(\
	connlist[0]\
	,connlist[1]\
	,connlist[2]\
	,connlist[3])

	return conn
