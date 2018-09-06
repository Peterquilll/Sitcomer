from flask import Flask
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


