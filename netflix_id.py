import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="Gospeed69", db="sitcome\
r")
cursor = db.cursor()

def add_id(n):
    query = "INSERT INTO episode (netlfix_id) VALUES (%s)"
    cursor.execute(query, (str(n)))

def main():
    n = 70273996
    e = 238
    for x in range(1, e):
        n +=1
        add_id(n)


if __name__ == '__main__':
    main()
