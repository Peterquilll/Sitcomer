import MySQLdb

import requests

from config import HOST, USER, PASSWD, DB


db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
cursor = db.cursor()

def grab_id():
    i = 0
    show = input("what show are we looking up chief: ")
    table_name = show.replace(" ", "_")
    cursor.execute("SELECT api_id from new_guidebox_data where show_name='" + str(show) +"'")
    api_id = [int(api_id[0]) for api_id in cursor.fetchall()]
    cursor.execute("SELECT number_of_seasons from shows where name_of_show='" + str(table_name) +"'")
    season = [int(season[0]) for season in cursor.fetchall()]
    seasons = range(1, season[0] + 1)
    print('All right, let me see what I can find')
    for i in seasons:
        print('Season:', i)
        print('I think I found something chief')
        api_call = requests.get("http://api-public.guidebox.com/v2/shows/" + str(api_id[0]) +
        "/episodes?&api_key=e40f887eaf55ce0cfca02259584e9a1eacbda97c&include_links=true&season="+ str(i) +"&limit=30")
        data = api_call.json()
        info = data['results']
        for result in info:
            if result['subscription_web_sources'][0]['source'] == 'python netflix':
                link = result['subscription_web_sources'][0]['link']
                query = ("UPDATE " + table_name +" set netflix_id=%s WHERE season_number=%s AND episode_number=%s")
                cursor.execute(query, (link[-8:], result['season_number'], result['episode_number']))
            elif result['subscription_web_sources'][1]['source'] == 'netflix':
                link = result['subscription_web_sources'][1]['link']
                query = ("UPDATE " + table_name +" set netflix_id=%s WHERE season_number=%s AND episode_number=%s")
                cursor.execute(query, (link[-8:], result['season_number'], result['episode_number']))

            db.commit()
            
    print('It is done chief')

def main():
    grab_id()


if __name__ == '__main__':
    main()
    
