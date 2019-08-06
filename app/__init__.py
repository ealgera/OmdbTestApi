from flask import Flask

app = Flask(__name__)

from app import routes  # Van de packahe, dus niet de variabele

app.run(port=5100, debug=True)