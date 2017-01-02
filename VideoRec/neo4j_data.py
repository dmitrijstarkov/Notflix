# This is a script to add movie data to the neo4J db
# currently i'ts adding both user, movie AND the fact it's watched.
# i need to modify it to only add the nodes.
# then the pyserver is the one that will need to create relationships based on node data

from py2neo import Graph,Node,Relationship
import os, json, requests, sys

def txCreate(obj):
	
	g = Graph("http://localhost:7474",password='admin')
	tx = g.begin()
	tx.create(obj)
	tx.commit()
	
def UserWatched(userid,filmid):

	import datetime
	
	# define what things are

	#MATCH (node:Label) RETURN node.property

	#match (Film) RETURN (Film.filmid)

	# i will need to "get" these from neo4j, right?..

	a = Node("User",userid=userid)
	b = Node("Film",filmid=filmid)
	ab = Relationship(a,"WATCHED",b,date=str(datetime.datetime.now()))
	
	txCreate(ab)
	
def AddVideos(video_id,video_type,director)
	
	video = Node("Video",video_id=video_id,video_type=video_type,director=director)
	txCreate(video)

def AddUsers(user_id):
	
	user = Node("User",user_id=user_id)
	txCreate(user)
	

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
