import random

import requests

import MySQLdb

from config import HOST, USER, PASSWD, DB


db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
cursor = db.cursor()

def get_episode(n):
    season_range = range(1, n + 1)
    season = random.choice(season_range)
    cursor.execute("SELECT season_number, episode_number, episode_name, episode_pic, netflix_id FROM episode WHERE season_number=" + str(season) + "")
    rows = cursor.fetchall()
    return random.choice(rows)


def main():
    n = 10
    print(str(get_episode(n)))


if __name__ == '__main__':
    main()
