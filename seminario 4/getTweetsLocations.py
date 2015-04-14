# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information on Twitter's OAuth implementation.

#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask import request
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
import twitter
import json
import sys

# Macros necesarias
CONSUMER_KEY = 'ZwvOETB1sZH02JknszNobMhlF'
CONSUMER_SECRET = 'yGuNtghvbUz2EOctdwNQzktxaqvCDgx0MosZFkzswbgJsvRXbC'
OAUTH_TOKEN = '589371810-g4tKuN81iSMEeG8odVmzPqgFZKkqSuE7x4FEzxCN'
OAUTH_TOKEN_SECRET = 'aVqCBJMyfDHA8dttltClRvVy9Gt8wZrnjtgC3RVOlHpQP'

app = Flask(__name__)
GoogleMaps(app)

# Consigue el API de Twitter
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

def getTweetsSearch(busqueda):
	#Limitamos la busqueda a Espana
	localizacion = "40.2085,-3.713,497mi"

	tweets = twitter_api.search.tweets(q=busqueda, count=1000, geocode=localizacion)

	aux = json.dumps(tweets, indent = 1)
	it = json.loads(aux)

	resultado = []
	for i in it['statuses']:
		if i['coordinates'] is not None:
			resultado.append(i['coordinates']['coordinates'][1])
			resultado.append(i['coordinates']['coordinates'][0])

	resultado = zip(resultado[0::1], resultado[1::2])
	return resultado

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/buscar", methods=['POST'])
def mapview():
	termino = request.form['text'] 
	coordenadas = getTweetsSearch(termino)
	
	search_results = twitter_api.search.tweets(q=termino, count='100')
	statuses = search_results['statuses']
	localizacion = "40.2085,-3.713,497mi"
	tweets = tweets_search_text(termino)
	
	mymap = Map(
		identifier="view-side",
		lat=40.3450396,
		lng=-3.6517684,
		markers=coordenadas,
		style="height:800px;width:800px;margin:0;"
	) 
	return render_template('mymap.html', mymap=mymap)

def tweets_search_text(text) :
    search_results = twitter_api.search.tweets(q=text, count='100')
    statuses = search_results['statuses']
    return statuses

if __name__ == "__main__":
    app.run(debug=True)
