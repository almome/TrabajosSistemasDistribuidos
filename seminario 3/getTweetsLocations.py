# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values
# for these credentials, which you'll need to provide in place of these
# empty string values that are defined as placeholders.
# See https://dev.twitter.com/docs/auth/oauth for more information on Twitter's OAuth implementation.

#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
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

# Busca los 100 primeros tweets que contengan el texto y la geolocalizacion introducida
def tweets_search_text(text, geo) :
    search_results = twitter_api.search.tweets(q=text, count='100', geocode=geo)
    statuses = search_results['statuses']
    return statuses
    
# Devuelve las coordenadas de los tweets
def get_tweets_coordinates(tweets) :
    coordinates = []
    for tweet in tweets :
        if tweet["coordinates"] is not None : # Si el tweet no tiene ese campo vacio
            coordinates.append([tweet["coordinates"].values()[1][1], tweet["coordinates"].values()[1][0]]) 
    return coordinates

# Se coge el texto y la geolocalizacion introducida en la linea de comandos o sino los valores por defecto, que es el texto Avengers y la geolocalizacion en el centro de USA alrededor de 20000 millas.
# Ejemplo: python searchTweets.py Hulk 134.5643,-5.7876,765mi
if len(sys.argv) >= 3 :
    text = sys.argv[1]
    geo = sys.argv[2]
else : 
    if len(sys.argv) == 2 :
        text = sys.argv[1]
        geo = "37.09024,-95.712891,20000mi"
    else :
        text = "Avengers"
        geo = "37.09024,-95.712891,20000mi"

# Main
tweets = tweets_search_text(text, geo)
coordinates = get_tweets_coordinates(tweets)
geoSplit = geo.split(",") # Dividimos para posteriormente poner la latitud y longitud correcta en la funcion para generar el mapa

@app.route("/")
def mapview():
    mymap = Map(
        identifier="view-side",
        lat=geoSplit[0],
        lng=geoSplit[1],
        markers=coordinates,
        style="height:800px;width:800px;margin:0;"
    ) 
    return render_template('mymap.html', mymap=mymap)


if __name__ == "__main__":
    app.run(debug=True)
