from flask import Flask
app = Flask(__name__)

from episodes import get_episode

@app.route("/")
def index():
    n = 10
    return str(get_episode(n))



