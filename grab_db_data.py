import requests

import MySQLdb

from config import HOST, USER, PASSWD, DB


db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
cursor = db.cursor()

def table_creator ():
    name = input("Name of table(use _ for spaces): ")
    query = "CREATE TABLE " + name + "( id INT NOT NULL AUTO_INCREMENT, season_number int, episode_numb\
er int, episode_name VARCHAR(200), episode_pic VARCHAR(200), netflix_id VARCHAR(200), show_description \
VARCHAR(2000), PRIMARY KEY (id) );"
    cursor.execute(query)
    db.commit()

def grab_db_show_id(show_title):
    db_id = requests.get("https://api.themoviedb.org/3/search/tv?api_key=dbaf6686a7c9d4d26e54ec02c635c530&language=en-US&query=" + show_title)
    id_query = db_id.json()
    show_details = id_query['results']
    for details in show_details:
        new_id = details['id']
        return str(new_id)

def grab_show_season(new_id):
    new_id = new_id
    season_query = requests.get('https://api.themoviedb.org/3/tv/'+ new_id +'?api_key=dbaf6686a7c9d4d26e54ec02c635c530')
    data = season_query.json()
    seasons = data['number_of_seasons']
    return(seasons)

def grab_episodes(show_title, new_id, seasons):
    episode_query = requests.get('https://api.themoviedb.org/3/tv/'+ new_id +'/season/' + str(seasons) + '?api_key=dbaf6686a7c9d4d26e54ec02c635c530')
    data = episode_query.json()
    episodes = data['episodes']
    for episode in episodes:
         query = "INSERT INTO " + show_title.replace(" ", "_") +" (season_number, episode_number, episode_name, show_description, episode_pic)VALUES (%s, %s, %s, %s, %s)"

         cursor.execute(query, (episode['season_number'], episode['episode_number'], episode['name'], episode['overview'], episode['still_path']))
    db.commit()
    
def update_show_db(show_title, seasons):
    query = ("INSERT INTO `show` (name_of_show, number_of_seasons) VALUES ('" + show_title.replace(" ", "_")  + "' ,"+ str(seasons) + ")")
    cursor.execute(query)
    db.commit()


    

def main():
    show_title = input("Name of the show(Please use spaces): ")
    new_id = grab_db_show_id(show_title)
    seasons = grab_show_season(new_id)
    table_creator()
    update_show_db(show_title, seasons)
    for x in range(1, seasons + 1):
        grab_episodes(show_title, new_id, x)


        
if __name__ == '__main__':
    main()

