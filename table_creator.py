import requests

import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="Gospeed69", db="sitcomer")
cursor = db.cursor()

def main():
    name = input("Name of table(Use _ for spaces): ")
    query = "CREATE TABLE " + name + "( id INT NOT NULL AUTO_INCREMENT, season_number int, episode_number int, episode_name VARCHAR(200), episode_pic VARCHAR(200), netflix_id VARCHAR(200), imdb_id VARCHAR(200), PRIMARY KEY (id) );"
    cursor.execute(query)
    db.commit()

if __name__ == '__main__':
    main()
