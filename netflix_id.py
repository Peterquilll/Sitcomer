import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="Gospeed69", db="sitcome\
r")
cursor = db.cursor()

def main():
    n = 70273996
    e = 239
    i = 1
    for x in range(1, e):
        n += 1
        my_list = str(n)
        query = "UPDATE episode SET netflix_id=%s WHERE id=%s"
        print(n)
        cursor.execute(query, (my_list, i))
        i += 1
        print(i)
    db.commit()



if __name__ == '__main__':
    main()
