import random

import requests

import MySQLdb

from config import HOST, USER, PASSWD, DB


db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
cursor = db.cursor()

def get_episode(n, show):
    n = n
    show = show
    cursor.execute("select number_of_seasons from shows where id="+ str(n) +"")
    seasons = [int(season[0]) for season in cursor.fetchall()]
    season_range = range(1, seasons[0] + 1)
    season_choice = random.choice(season_range)
    cursor.execute("SELECT season_number, episode_number, episode_name, episode_pic, show_description, netflix_id FROM "+ show + " WHERE season_number=" + str(season_choice) + "")
    rows = cursor.fetchall()
    db.commit()
    return random.choice(rows)
    
def get_length():
    cursor.execute("SELECT id from shows order by id DESC LIMIT 1")
    length = [int(season[0]) for season in cursor.fetchall()]
    i = random.randrange(0, length[0])
    query = ("SELECT name_of_show FROM shows where id=%s")
    cursor.execute(query, [(str(i))])
    rows = cursor.fetchall()
    show = ''.join(rows[0])
    return(i, show)
