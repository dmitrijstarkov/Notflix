import os, json, shutil

from funcs import s, metadata, omdb, db_post, get, put_place, delete, hashing, collection_check, pathtodo, pathtoput
from movies import movie
from series import tv
from rest_config import film_login, series_login, episode_login\
, FILM_URL, EPISODE_URL, SERIES_URL

for dirname, dirnames, filenames in os.walk(pathtodo):
	for subdirname in dirnames:
		if subdirname == "tmp" or subdirname == 'todo':
			continue
		else:
			newname = hashing(subdirname,pathtodo)
			imdb = metadata(newname,pathtodo)
			print('getting data for '+imdb+' in folder '+newname)
			vid_meta = omdb(imdb)
			vid_meta['server_url'] = "http://localhost:81/"+newname+"/manifest.mpd"
			
			vidtitle,vidtype=s(vid_meta['Title']),s(vid_meta['Type'])

			shutil.move(pathtodo+'/'+newname, pathtoput+'/'+newname)
			print(s(newname)+' folder moved to '+s(pathtoput))

			# put / post movie data
			
			print(vidtype)
			
			if vidtype=="movie":

				movie(vid_meta,vidtitle,FILM_URL,film_login)
			
			elif vidtype =="episode" and s(vid_meta['seriesID']) != 'N/A':
				
				series_meta = omdb(s(vid_meta['seriesID']))
				series_title = series_meta['Title']

				tv(series_meta,series_title,SERIES_URL,series_login)
				tv(vid_meta,series_title,EPISODE_URL,episode_login)