from funcs import put_place, get, collection_check, s, db_post
	
def tv(data1,str1,url,login):

	DB = url + '/series'
	if get(DB,login) == '404':
		put_place(DB)
		print('putting' + s(DB))
		
	COLL = DB +'/'+str1
	collection_check(COLL,login)
	db_post(COLL,data1,login)
	