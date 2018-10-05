import MySQLdb

from config import HOST, USER, PASSWD, DB


db = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWD, db=DB)
cursor = db.cursor()

def main():
    show_name = input("name of show: ")
    n = input("netlfix id - 1: ")
    e = input("number of episodes to change + 1: ")
    i = input("(which episode do you want to start at?(1 for default): ")
    for x in range(1, int(e)):
        n = int(n)
        i = int(i)
        n += 1
        my_list = str(n)
        query = "UPDATE "+ show_name + " SET netflix_id=%s WHERE id=%s"
        print(n)
        cursor.execute(query, (my_list, i))
        i += 1
        print(i)
    db.commit()



if __name__ == '__main__':
    main()
