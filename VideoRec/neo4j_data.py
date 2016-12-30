# This is a script to add movie data to the neo4J db

import os
import json
import requests

_BASE_URL = "http://localhost:90" # CHANGEIT
VIDEO_HEADERS = {'Content-type': 'application/hal+json', 'Accept': '*/*'}


coll = requests.get(_BASE_URL+'/movie',data=None,auth=('admin','changeit')).json()['_embedded']['rh:coll']

print(coll)

listicle = [j.items()[0][1] for i,j in enumerate(coll)]

#print(listicle)

data = {i:requests.get(_BASE_URL+'/movie/'+str(i),data=None,auth=('admin','changeit')).json()['_embedded']['rh:doc'][0] for i in listicle}

#print(data)

things = \
['Director','Writer','Actors','Genre','Language','Country'\
,'Runtime','Rated','imdbVotes','imdbRating']


for i,j in enumerate(things):
	print(i,j)

listy = {j : {q:data[j][q] for p,q in enumerate(things)} for i,j in enumerate(data)}

print(listy)

#for i,j in enumerate(data):
#	print(i,j)
#	print(data[j]['Director'].split(', '))
#	print(data[j]['Writer'].split(', '))
#	print(data[j]['Actors'].split(', '))
#	print(data[j]['Genre'].split(', '))
#	print(data[j]['Language'].split(', '))
#	print(data[j]['Country'].split(', '))
#	print(data[j]['Runtime'])
#	print(data[j]['Rated'])
#	print(data[j]['imdbVotes'])
#	print(data[j]['imdbRating'])