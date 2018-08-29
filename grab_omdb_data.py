import requests

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="Gospeed69", db="sitcomer")
cursor = db.cursor()


def grab_omdb_data(n):
    response = requests.get("http://www.omdbapi.com/?i=tt0108778&season=" + str(n) + "&y=2000&apikey=b6762ffb")
    data = response.json()
    episodes = data['Episodes']
    for episode in episodes:
        query = "INSERT INTO episode (season_number, episode_number, episode_name, imdb_id) VALUES (%s, %s, %s, %s)"

        cursor.execute(query, (str(n), episode['Episode'] ,episode['Title'], episode['imdbID']))

    db.commit()


def main():
    n = 10
    for x in range(1, n+1):
        grab_omdb_data(x)


if __name__ == '__main__':
    main()
