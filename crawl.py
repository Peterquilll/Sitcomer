import requests

import MySQLdb

from bs4 import BeautifulSoup

db = MySQLdb.connect(host="localhost", user="root", \
passwd="Gospeed69", db="sitcomer")
cursor = db.cursor()
 
def scrape(n):
    i = 1
    response = requests.get("https://www.imdb.com/title/tt0108778/episodes?season=" +str(n) + "")
    html_soup = BeautifulSoup(response.text, 'html.parser')
    images = html_soup.find_all('img', class_='zero-z-index')
    img = images
    for image in images:
        query = "UPDATE episode SET episode_pic=%s WHERE season_number=%s AND episode_number=%s"
        print('query: ', query)
        cursor.execute(query, (image.attrs['src'], str(n), i))
        i +=1
    db.commit()
    

def main():
    n = 10
    for x in range(1, n + 1):
        scrape(x)

if __name__ == '__main__':
    main()
    
