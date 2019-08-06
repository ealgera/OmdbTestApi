from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes  # Van de packahe, dus niet de variabele

app.run(port=5100, debug=True)