from funcs import s, metadata, omdb, db_post, get, put_place, delete, hashing, collection_check, pathtodo, pathtoput
import os, json, shutil
from video_api import _BASE_URL


MOVIE_DB,TV_DB,SERIES_DB = \
_BASE_URL + '/movie',\
_BASE_URL + '/episode',\
_BASE_URL + '/series'


print('--------------------')
#ALL_DBS = [MOVIE_DB,TV_DB,SERIES_DB]
#for i in ALL_DBS:
#	delete(i)
#	put_place(i)
print('--------------------')

for dirname, dirnames, filenames in os.walk(pathtodo):
	for subdirname in dirnames:
		if subdirname == "tmp" or subdirname == 'todo':
			continue
		else:
			
			# rename the folder as an md5 hash value
			# then go get data from the imdbID in the metadata.txt file
			# add in the server location of the .mpd file
			
			newname = hashing(subdirname,pathtodo)
			imdb = metadata(newname,pathtodo)
			print('getting data for '+imdb+' in folder '+newname)
			vid_meta = omdb(imdb)
			vid_meta['server_url'] = "http://localhost:81/"+newname+"/manifest.mpd"
			
			vidtitle,vidtype=s(vid_meta['Title']),s(vid_meta['Type'])

			# put / post movie data
			
			if vidtype=="movie":

				FILM_COLL = MOVIE_DB +'/'+vidtitle
				put_place(FILM_COLL)
				filmpost = db_post(FILM_COLL,vid_meta)

			# put / post tv show data
			
			elif vidtype =="episode" and s(vid_meta['seriesID']) != 'N/A':
				
				series_meta = omdb(s(vid_meta['seriesID']))
				series_title = series_meta['Title']

				SERIES_COLL = TV_DB +'/'+series_title
				collection_check(SERIES_COLL)
				episodepost=db_post(SERIES_COLL,vid_meta)

				SERIES_NFO_COLL = SERIES_DB +'/'+series_title
				collection_check(SERIES_NFO_COLL)
				seriespost=db_post(SERIES_NFO_COLL,series_meta)

			# move the folder to /encoded_video folder
			# it's now ready to be streamed...

			shutil.move(pathtodo+'/'+newname, pathtoput+'/'+newname)
			print(s(newname)+' folder moved to '+s(pathtoput))