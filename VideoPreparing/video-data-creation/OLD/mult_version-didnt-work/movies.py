from funcs import put_place, get, s, db_post
	
def movie(vid_meta,vidtitle,FILM_URL,film_login):

	MOVIE_DB = FILM_URL + '/movie'
	if get(MOVIE_DB,film_login) == '404':
		put_place(MOVIE_DB)
		print('putting' + s(MOVIE_DB))
		
	FILM_COLL = FILM_URL +'/movie/'+vidtitle
	put_place(FILM_COLL,film_login)
	print('putting collection' + s(FILM_COLL))
	
	filmpost = db_post(FILM_COLL,vid_meta,film_login)
	print('putting movie data' + s(FILM_COLL))