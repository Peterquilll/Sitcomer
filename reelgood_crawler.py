import MySQLdb

from config import HOST, USER, PASSWD, DB

from bs4 import BeautifulSoup

import requests

db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
cursor = db.cursor()

def grab_keys():
    



def main():
    pass

if __name__ == '__main__':
    main()
