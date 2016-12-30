from funcs import s, metadata, omdb, db_post, get, put_place, delete, hashing
from video_api import _BASE_URL
import os, json

MOVIEDB,TV_DB = _BASE_URL + '/movie',_BASE_URL + '/episode'

print('--------------------')
delete(MOVIEDB)
delete(TV_DB)
print('--------------------')

for dirname, dirnames, filenames in os.walk('.'):
	for subdirname in dirnames:
		if subdirname == "tmp" or subdirname == 'todo':
			continue
		elif '.git' in dirnames:
			dirnames.remove('.git')
		else:			

			imdb = metadata(subdirname)
			vid_meta = omdb(imdb)
			vid_meta['server_url'] = "http://localhost:81/"+subdirname+"/manifest.mpd"
			vidtitle,vidtype=s(vid_meta['Title']),s(vid_meta['Type'])
			
			if vidtype=="movie":

				FILM_COLL = MOVIEDB +'/'+vidtitle
				put_place(FILM_COLL)
				filmpost = db_post(FILM_COLL,vid_meta)
			
			elif vidtype =="episode" and vid_meta['seriesID'] != 'N/A':
				
				series_title = omdb(vid_meta['seriesID'])['Title']
				SERIES_COLL = MOVIEDB +'/'+series_title
				coll = get(SERIES_COLL)

				if coll.status_code == 404:
					
					print("Coll gave a 404 response. Adding series: "+series_title)
					make_coll = put_place(SERIES_COLL)

				episodepost=db_post(SERIES_COLL,vid_meta)
			hashing(subdirname)