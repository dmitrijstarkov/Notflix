# This is a script to add movie data to the neo4J db
# currently i'ts adding both user, movie AND the fact it's watched.
# i need to modify it to only add the nodes.
# then the pyserver is the one that will need to create relationships based on node data

from py2neo import Graph, Node, Relationship
import os, json, requests, sys

g = Graph("http://rec_server",password='admin')

def txCreate(obj):
	
	tx = g.begin()
	tx.exists
	tx.create(obj)
	tx.commit()

def txMerge(obj):
	
	tx = g.begin()
	tx.exists
	tx.merge(obj)
	tx.commit()
	
def relate(type1,type2,id1,id2,rel):

	a = Node(type1,title=id1)
	b = Node(type2,title=id2)
	ab = Relationship(a,rel,b)
	
	txCreate(ab)
	
def AddVideos(video_id,video_type,director):
	
	video = Node("Video",video_id=video_id,video_type=video_type,director=director)
	txCreate(video)

def AddUsers(user_id):
	
	user = Node("User",user_id=user_id)
	txCreate(user)
	
def repeat_create(thing,thingstring,relate,videonode):
	for i,j in enumerate(thing):

		thingnode = Node(thingstring,title=thing[i],id=thing[i])
		txMerge(thingnode)
		rel = Relationship(thingnode,relate,videonode)
		txMerge(rel)


_BASE_URL = "http://video-rest:8080" # CHANGEIT
VIDEO_HEADERS = {'Content-type': 'application/hal+json', 'Accept': '*/*'}

coll = requests.get(_BASE_URL+'/movie',data=None,auth=('admin','changeit')).json()['_embedded']['rh:coll']

#print(coll)

listicle = [j.items()[0][1] for i,j in enumerate(coll)]

#print(listicle)

data = {i:requests.get(_BASE_URL+'/movie/'+str(i),data=None,auth=('admin','changeit')).json()['_embedded']['rh:doc'][0] for i in listicle}

for i,j in enumerate(data):
	print(i,j)


	title = str(data[j].items()[2][1])
	imdbid = str(data[j].items()[17][1])
	imdbrating = str(data[j].items()[19][1]).split('.')[0]
	vidtype = str(data[j].items()[5][1])

	writers = data[j].items()[3][1].split(', ')
	actors = data[j].items()[4][1].split(', ')
	directors = data[j].items()[8][1].split(', ')
	genres = data[j].items()[11][1].split(', ')

	print(title)
	print(imdbid)
	print(imdbrating)
	print(vidtype)

	print(writers)
	print(actors)
	print(directors)
	print(genres)


	videonode =\
	Node(\
	str(vidtype)\
	,title=title\
	,id=imdbid\
	,score=imdbrating\
	)

	print(videonode)


	repeat_create(writers,"writer","WROTE",videonode)
	repeat_create(actors,"actor","ACTED IN",videonode)
	repeat_create(directors,"director","DIRECTED",videonode)
	repeat_create(genres,"genre","GENRE",videonode)

#for i,j in enumerate(actors):
#	txCreate(Node("actor",actor=actors[i]))
#	print(Node("actor",actor=actors[i]))

#for i,j in enumerate(directors):
#	txCreate(Node("director",director=directors[i]))
#	print(Node("director",director=directors[i]))

#for i,j in enumerate(genres):
#	txCreate(Node("genre",genre=genres[i]))
#	print(Node("genre",genre=genres[i]))


# TOGET - movies

# Title - node
# Writer(s) - node
# Actors(s) - node
# Director(s) - node
# Genre(s) - node
# Rated - title property
# imdbid - title property?
# imdbrating - title property? Node? - films over 9, over 8 etc?

# RELATIONSHIPS - videos

# Acted in
# Wrote
# Directed
# Genre?

filmid = 'tt023850'

#UserWatched(userid,filmid)
