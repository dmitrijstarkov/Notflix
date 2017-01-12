import MySQLdb

logins_mysql_user = 'root'
logins_mysql_ps = 'pw'
logins_mysql_db = 'logins_db'
logins_mysql_host = '172.17.0.5'
logins_mysql_port = 3306

logins_mysql_conn_list = ["172.17.0.4","root","pw","logins_db"]
payments_mysql_conn_list = ["172.17.0.6","root","pw","payment_db"]
subs_mysql_conn_list = ["172.17.0.5","root","pw","subscription_db"]


logins_conn = MySQLdb.connect(\
logins_mysql_conn_list[0]\
,logins_mysql_conn_list[1]\
,logins_mysql_conn_list[2]\
,logins_mysql_conn_list[3])

payments_conn = MySQLdb.connect(\
payments_mysql_conn_list[0]\
,payments_mysql_conn_list[1]\
,payments_mysql_conn_list[2]\
,payments_mysql_conn_list[3])

subs_conn = MySQLdb.connect(\
subs_mysql_conn_list[0]\
,subs_mysql_conn_list[1]\
,subs_mysql_conn_list[2]\
,subs_mysql_conn_list[3])


logins_cursor = logins_conn.cursor()
payments_cursor = payments_conn.cursor()
subs_cursor = subs_conn.cursor()