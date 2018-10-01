import requests

import MySQLdb

from bs4 import BeautifulSoup

from config import HOST, USER, PASSWD, DB, shows


db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
cursor = db.cursor()
 
def scrape(n, imdb_id, show_name):
    i = 1
    response = requests.get("https://www.imdb.com/title/"+ imdb_id + "/episodes?season=" +str(n) + "")
    html_soup = BeautifulSoup(response.text, 'html.parser')
    images = html_soup.find_all('img', class_='zero-z-index')
    img = images
    for image in images:
        query = "UPDATE " + show_name + " SET episode_pic=%s WHERE season_number=%s AND episode_number=%s"
        print('query: ', query)
        cursor.execute(query, (image.attrs['src'], str(n), i))
        i +=1
    db.commit()
    

def main():
    show_name = input("show name(use _ for spaces: ")
    imdb_id = input("imdb_id:")
    n = input("number of seasons:")
    for x in range(1, int(n) + 1):
        scrape(x, imdb_id, show_name)
        shows.append(show_name, str(n)

if __name__ == '__main__':
    main()
    
