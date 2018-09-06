from flask import Flask, send_from_directory
app = Flask(__name__)

from episodes import get_episode

from code import page

@app.route("/")
def index():
    n = 10
    episode_data = get_episode(n)
    image = episode_data[-1]
    img_html = '<img height="210" width="320" src="%s" />' % (image,)
    result = page() + img_html + str(episode_data[:-1]) + '</body></html>'
    return result


@app.route("/vendor/<path:path>")
def send_vendor(path):
    return send_from_directory('vendor', path)

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('css', path)

@app.route("/img/<path:path>")
def send_img(path):
    return send_from_directory('img', path)
