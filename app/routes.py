from flask import render_template, request, url_for, flash
from app import app  # De variabele...
from app.forms import LoginForm, SearchForm
import requests

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Eric"}
    return render_template("index.html", title="Zoeken naar Films", user=user)

@app.route("/batman/<movie>")
def batman_movies(movie):
    omdb_api_key = "6c3df824"
    url = "http://www.omdbapi.com/"
    search_for = movie
    req_url = url + "?s=" + search_for + "&apikey=" + omdb_api_key
    #print(req_url)
    my_req = requests.get(req_url).json()
    return render_template("batman.html", title="Batman films", films=my_req)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        return batman_movies(form.search_field.data)
    else:
        if request.method == "POST":
            flash("Je moet het zoekveld invullen...", category="danger")

    return render_template("search.html", title="Zoeken", form=form)