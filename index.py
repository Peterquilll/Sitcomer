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

@app.route("/anime")
def anime():
    return render_template('anime.html')

@app.route("/classic_sitcom")
def classic():
    return render_template('classic.html')

@app.route("/comedy")
def comedy():
    return render_template('comedy.html')

@app.route("/crime_drama")
def crime():
    return render_template('crime.html')

@app.route("/dc_originals")
def dc():
    return render_template('dc.html')

@app.route("/drama")
def drama():
    return render_template('drama.html')

@app.route("/marvel_originals")
def marvel():
    return render_template('marvel.html')

@app.route("/netflix_originals")
def originals():
    return render_template('originals.html')

@app.route("/romcom")
def romcom():
    return render_template('romcom.html')

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
    episode_data = get_episode(8, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/mad_men")
def mad():
    show = 'mad_men'
    episode_data = get_episode(9, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/twin_peaks")
def twin():
    show = 'twin_peaks'
    episode_data = get_episode(19, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_twilight_zone")
def twilight():
    show = 'the_twilight_zone'
    episode_data = get_episode(10, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/bojack_horseman")
def bojack():
    show = 'bojack_horseman'
    episode_data = get_episode(11, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/oitnb")
def orange():
    show = 'orange_is_the_new_black'
    episode_data = get_episode(12, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_west_wing")
def west():
    show = 'the_west_wing'
    episode_data = get_episode(13, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/sherlock")
def sherlock():
    show = 'sherlock'
    episode_data = get_episode(14, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/stranger_things")
def stranger():
    show = 'stranger_things'
    episode_data = get_episode(16, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/unbreakable_kimmy_schmidt")
def unbreakable():
    show = 'unbreakable_kimmy_schmidt'
    episode_data = get_episode(17, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/jessica_jones")
def jessica():
    show = 'jessica_jones'
    episode_data = get_episode(15, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_good_place")
def good():
    show = 'the_good_place'
    episode_data = get_episode(18, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/that_70s_show")
def that_show():
    show = 'that_70s_show'
    episode_data = get_episode(20, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/nashville")
def nashville():
    show = 'nashville'
    episode_data = get_episode(21, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/13_reasons_why")
def reasons():
    show = '13_reasons_why'
    episode_data = get_episode(22, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/greys_anatomy")
def greys():
    show = 'greys_anatomy'
    episode_data = get_episode(23, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/one_punch")
def punch():
    show = 'one_punch'
    episode_data = get_episode(24, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/death_note")
def death():
    show = 'death_note'
    episode_data = get_episode(25, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/naruto")
def naruto():
    show = 'naruto'
    episode_data = get_episode(26, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/soul_eater")
def soul():
    show = 'soul_eater'
    episode_data = get_episode(27, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/bleach")
def bleach():
    show = 'bleach'
    episode_data = get_episode(28, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_flash")
def flash():
    show = 'the_flash_'
    episode_data = get_episode(29, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/supergirl")
def supergirl():
    show = 'supergirl'
    episode_data = get_episode(30, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/arrow")
def arrow():
    show = 'arrow'
    episode_data = get_episode(31, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/black_lightning")
def lightning():
    show = 'black_lightninig'
    episode_data = get_episode(32, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/legends_of_tomorrow")
def legends():
    show = 'legends_of_tomorrow'
    episode_data = get_episode(33, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/gotham")
def gotham():
    show = 'gotham'
    episode_data = get_episode(34, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/daredevil")
def daredevil():
    show = 'daredevil'
    episode_data = get_episode(35, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/luke_cage")
def luke():
    show = 'luke'
    episode_data = get_episode(36, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/iron_fist")
def iron():
    show = 'iron_fist'
    episode_data = get_episode(37, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/defenders")
def defenders():
    show = 'defenders'
    episode_data = get_episode(38, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/punisher")
def punisher():
    show = 'punisher'
    episode_data = get_episode(39, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/agents_of_shield")
def agents():
    show = 'agents_of_shield'
    episode_data = get_episode(40, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/new_girl")
def new():
    show = 'new_girl'
    episode_data = get_episode(41, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/american_horror_story")
def horror():
    show = 'american_horror_story'
    episode_data = get_episode(42, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/portlandia")
def portlandia():
    show = 'portlandia'
    episode_data = get_episode(43, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/frasier")
def frasier():
    show = 'frasier'
    episode_data = get_episode(44, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/shameless")
def shameless():
    show = 'shameless'
    episode_data = get_episode(45, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_it_crowd")
def it():
    show = 'the_it_crowd'
    episode_data = get_episode(46, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/better_call_saul")
def saul():
    show = 'saul'
    episode_data = get_episode(47, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/parts_unknown")
def parts():
    show = 'parts_unknown'
    episode_data = get_episode(48, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/peaky_blinders")
def peaky():
    show = 'peaky_blinders'
    episode_data = get_episode(49, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/califonication")
def californication():
    show = 'californication'
    episode_data = get_episode(50, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)


@app.route("/house_of_cards")
def cards():
    show = 'house_of_cards'
    episode_data = get_episode(51, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/gilmore_girls")
def gilmore():
    show = 'gilmore_girls'
    episode_data = get_episode(52, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_walking_dead")
def walking():
    show = 'the_walking_dead'
    episode_data = get_episode(53, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/black_list")
def black_list():
    show = 'black_list'
    episode_data = get_episode(54, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/izombie")
def izombie():
    show = 'izombie'
    episode_data = get_episode(55, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/black_mirror")
def black_mirror():
    show = 'black_mirror'
    episode_data = get_episode(56, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/jane_the_virgin")
def jane():
    show = 'jane_the_virgin'
    episode_data = get_episode(57, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/glee")
def glee():
    show = 'glee'
    episode_data = get_episode(58, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/skins")
def skins():
    show = 'skins'
    episode_data = get_episode(59, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_vampire_diaries")
def vampire():
    show = 'the_vampire_diaries'
    episode_data = get_episode(60, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/pretty_litte_liars")
def pretty():
    show = 'pretty_little_liars'
    episode_data = get_episode(61, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/charmed")
def charmed():
    show = 'charmed'
    episode_data = get_episode(62, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/scandal")
def scandal():
    show = 'scandal'
    episode_data = get_episode(63, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/sons_of_anarchy")
def sons():
    show = 'sons_of_anarchy'
    episode_data = get_episode(64, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/how_to_get_away_with_murdur")
def how_to():
    show = 'how_to_get_away_with_murder'
    episode_data = get_episode(65, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/luther")
def luther():
    show = 'luther'
    episode_data = get_episode(66, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/broadchurch")
def broadchurch():
    show = 'broadchurch'
    episode_data = get_episode(67, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/star_trek_the_next_generation")
def star_trek():
    show = 'star_trek_the_next_generation'
    episode_data = get_episode(68, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/riverdale")
def riverdale():
    show = 'riverdale'
    episode_data = get_episode(69, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/voltron_legendary_defender")
def voltron():
    show = 'voltron_legendary_defender'
    episode_data = get_episode(70, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/blue_mountain_state")
def blue():
    show = 'blue_mountain_state'
    episode_data = get_episode(71, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_inbetweeners")
def inbetween():
    show = 'the_inbetweeners"'
    episode_data = get_episode(72, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/trailer_park_boys")
def trailer():
    show = 'trailer_park_boys'
    episode_data = get_episode(73, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/episodes")
def episodes():
    show = 'episodes'
    episode_data = get_episode(74, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_andy_griffith_show")
def andy():
    show = 'the_andy_griffith_show'
    episode_data = get_episode(75, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/atypical")
def atypical():
    show = 'atypical'
    episode_data = get_episode(76, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/love")
def love():
    show = 'love'
    episode_data = get_episode(77, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/crazy_ex_girlfriend")
def ex():
    show = 'crazy_ex_girlfriend'
    episode_data = get_episode(78, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/santa_clarita_diet")
def santa():
    show = 'santa_clarita_diet'
    episode_data = get_episode(79, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_ranch")
def the_ranch():
    show = 'the_ranch'
    episode_data = get_episode(80, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_good_cop")
def cop():
    show = 'the_good_cop'
    episode_data = get_episode(81, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/fuller_house")
def fuller():
    show = 'fuller_house'
    episode_data = get_episode(82, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/parenthood")
def parenthood():
    show = 'parenthood'
    episode_data = get_episode(83, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/weeds")
def weeds():
    show = 'weeds'
    episode_data = get_episode(84, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/ozark")
def ozark():
    show = 'ozark'
    episode_data = get_episode(85, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_crown")
def crown():
    show = 'the_crown'
    episode_data = get_episode(86, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_100")
def the_100():
    show = 'the_100'
    episode_data = get_episode(87, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/once_upon_a_time")
def time():
    show = 'once_upon_a_time'
    episode_data = get_episode(88, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/law_and_order_svu")
def law():
    show = 'law_and_order_special_victims_unit'
    episode_data = get_episode(89, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/grace_and_frankie")
def grace():
    show = 'grace_and_frankie'
    episode_data = get_episode(90, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/ncis")
def ncis():
    show = 'ncis'
    episode_data = get_episode(91, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/spartacus")
def spartacus():
    show = 'spartacus'
    episode_data = get_episode(92, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/narcos")
def narcos():
    show = 'narcos'
    episode_data = get_episode(93, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/call_the_midwife")
def midwife():
    show = 'call_the_midwife'
    episode_data = get_episode(94, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/the_get_down")
def get_down():
    show = 'the_get_down'
    episode_data = get_episode(95, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/bloodline")
def bloodline():
    show = 'bloodline'
    episode_data = get_episode(96, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/sense8")
def sense8():
    show = 'sense8'
    episode_data = get_episode(97, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/penny_dreadful")
def penny():
    show = 'penny_dreadful'
    episode_data = get_episode(98, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/nurse_jackie")
def nurse():
    show = 'nurse_jackie'
    episode_data = get_episode(99, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/criminal_minds")
def criminal():
    show = 'criminal_minds'
    episode_data = get_episode(100, show)
    netflix_id = episode_data[-1]
    season, episode, name, image, description = episode_data[:-1]
    return render_template('index.html', value=image, data_from_directory=episode_data, episode_name=name, season=season, episode=episode, netflix=netflix_id,description=description)

@app.route("/dexter")
def dexter():
    show = 'dexter'
    episode_data = get_episode(101, show)
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

