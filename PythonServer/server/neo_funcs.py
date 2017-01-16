from py2neo import Graph
from funcs import unique


g = Graph("http://rec_server",password='admin')


def reccomendations(in1):

	data = g.run(\
	"MATCH ("+in1+")-[:GENRE]->(relatedfilms) \
	return relatedfilms").data()
	data2 = data[1:(len(data)-1)]
	recs_list = unique([i.items()[0][1]['title'] for i in data[1:(len(data)-1)]])
	return recs_list