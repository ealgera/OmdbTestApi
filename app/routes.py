from flask import render_template
from app import app  # De variabele...
import requests

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Eric"}
    return render_template("index.html", title="Zoeken naar Films", user=user)

@app.route("/batman")
def batman_movies():
    omdb_api_key = "6c3df824"
    url = "http://www.omdbapi.com/"
    search_for = "Batman"
    req_url = url + "?s=" + search_for + "&apikey=" + omdb_api_key

    my_req = requests.get(req_url).json()
    return render_template("batman.html", title="Batman films", films=my_req)