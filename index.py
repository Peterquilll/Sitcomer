import functools

from config import shows

from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for, send_from_directory, render_template
app = Flask(__name__)

from episodes import get_episode

@app.route("/")
def choose_show ():
    return render_template('first_page.html', )

@app.route("/parks")
def parks():
    episode_data = get_episode(0, shows)
    netflix_id = episode_data[-1]
    season, episode, name, image = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id)

@app.route("/the_office")
def office():
    episode_data = get_episode(1, shows)
    netflix_id = episode_data[-1]
    season, episode, name, image = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id)

@app.route("/breaking_bad")
def bad():
    episode_data = get_episode(2, shows)
    netflix_id = episode_data[-1]
    season, episode, name, image = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id)

@app.route("/friends")
def friends():
    episode_data = get_episode(3, shows)
    netflix_id = episode_data[-1]
    season, episode, name, image = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id)

@app.route("/random")
def random ():
    import random
    i = random.randrange(0,3)
    episode_data = get_episode(i, shows)
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
