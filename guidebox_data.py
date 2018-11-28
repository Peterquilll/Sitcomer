import requests

import MySQLdb

from config import HOST, USER, PASSWD, DB


db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
cursor = db.cursor()

def grab_data():
    reelgood = requests.get('http://api-public.guidebox.com/v2/shows?limit=250&api_key=e40f887eaf55ce0cfca02259584e9a1eacbda97c&sources=netflix')
    data = reelgood.json()
    info = data['results']
    for result in info:
        query = "INSERT INTO new_guidebox_data (show_name, api_id)VALUES (%s, %s)"
        cursor.execute(query, (result['title'], result['id']))
    db.commit()

def main():
    grab_data()

if __name__ == '__main__':
    main()
    
