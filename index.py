from flask import Flask, send_from_directory, render_template
app = Flask(__name__)

from episodes import get_episode


@app.route("/")
def index():
    n = 10
    episode_data = get_episode(n)
    netflix_id = episode_data[-1]
    season, episode, name, image = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id)

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('css', path)

@app.route("/vendor/<path:path>")
def send_vendor(path):
    return send_from_directory('vendor', path)


if __name__ == '__main__':
   app.run(debug = True)
