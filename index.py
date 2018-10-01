import functools

from flask import Flask, Blueprint, flash, g, redirect, render_template, request, session, url_for, send_from_directory, render_template
app = Flask(__name__)

from get_episode import get_episode, get_length
# Main page
@app.route("/")
def choose_show ():
    return render_template('first_page.html', )

#pages
@app.route("/animated")
def animated():
    return render_template('animated.html')

@app.route("/classic_sitcom")
def classic():
    return render_template('classic.html')

@app.route("/comedy")
def comedy():
    return render_template('comedy.html')

@app.route("/drama")
def drama():
    return render_template('drama.html')

@app.route("/netflix_originals")
def originals():
    return render_template('originals.html')


# Shows
@app.route("/breaking_bad")
def bad():
    show = 'breaking_bad'
    episode_data = get_episode(2, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id, description=description)

@app.route("/friends")
def friends():
    show = 'friends'
    episode_data = get_episode(3, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id, description=description)

@app.route("/parks_and_rec")
def parks():
    show = 'parks_and_recreation'
    episode_data = get_episode(4, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id, description=description)

@app.route("/the_office")
def office():
    show = 'the_office'
    episode_data = get_episode(5, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id, description=description )

@app.route("/arrested_development")
def arrested():
    show = 'arrested_development'
    episode_data = get_episode(1, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/swtcl")
def the_clone_wars():
    show = 'the_clone_wars'
    episode_data = get_episode(6, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/cheers")
def cheers():
    show = 'cheers'
    episode_data = get_episode(7, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/master_of_none")
def master():
    show = 'master_of_none'
    episode_data = get_episode(15, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)



@app.route("/random")
def random ():
    import random
    i, show = get_length()
    episode_data = get_episode(i, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

#extra pages

@app.route("/coming_soon")
def soon():
    return render_template('coming_soon.html')

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('css', path)

@app.route("/vendor/<path:path>")
def send_vendor(path):
    return send_from_directory('vendor', path)


if __name__ == '__main__':
   app.run(debug = True)
