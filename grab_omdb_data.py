import requests

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="Gospeed69", db="sitcomer")
cursor = db.cursor()


def grab_omdb_data(show_title, show_id, n):
    response = requests.get("http://www.omdbapi.com/?i=" + show_id + "&season=" + str(n) + "&y=2000&apikey=b6762ffb")
    data = response.json()
    episodes = data['Episodes']
    for episode in episodes:
        query = "INSERT INTO " + show_title +" (season_number, episode_number, episode_name, imdb_id) VALUES (%s, %s, %s, %s)"

        cursor.execute(query, (str(n), episode['Episode'] ,episode['Title'], episode['imdbID']))

    db.commit()


def main():
    show_title = input("Name of the show(use _ for spaces):")
    show_id = input("IMDB ID:")
    n = input("number of seasons:")
    for x in range(1, int(n)+1):
        grab_omdb_data(show_title, show_id, x)


if __name__ == '__main__':
    main()
