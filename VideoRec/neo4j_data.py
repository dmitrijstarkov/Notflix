# This is a script to add movie data to the neo4J db
import sys
from py2neo import Graph,Node,Relationship
import os
import json
import requests

def UserWatched(userid,filmid):

	import datetime
	
	# define what things are

	g = Graph("http://localhost:7474",password='admin')
	a = Node("User",userid=userid)
	b = Node("Film",filmid=filmid)
	ab = Relationship(a,"WATCHED",b,date=str(datetime.datetime.now()))
	
	# put the things
	
	tx = g.begin()
	tx.create(a)
	tx.create(b)
	tx.create(ab)
	
	# commit the puts
	
	tx.commit()


_BASE_URL = "http://localhost:90" # CHANGEIT
VIDEO_HEADERS = {'Content-type': 'application/hal+json', 'Accept': '*/*'}

coll = requests.get(_BASE_URL+'/movie',data=None,auth=('admin','changeit')).json()['_embedded']['rh:coll']

#print(coll)

listicle = [j.items()[0][1] for i,j in enumerate(coll)]

#print(listicle)

data = {i:requests.get(_BASE_URL+'/movie/'+str(i),data=None,auth=('admin','changeit')).json()['_embedded']['rh:doc'][0] for i in listicle}

#print(data)

things = \
['Director','Writer','Actors','Genre','Language','Country'\
,'Runtime','Rated','imdbVotes','imdbRating']

#for i,j in enumerate(things):
#	print(i,j)

listy = {j : {q:data[j][q] for p,q in enumerate(things)} for i,j in enumerate(data)}

#print(listy)

##### NEO 4 J stuff:

print(listy.keys()[0])
#print(listy.items()[0][1]['Genre'].split(', '))
print(listy.items()[0][1]['Rated'])

userid = 'akjghf2895762957389587'
filmid = 'tt023850'

UserWatched(userid,filmid)
