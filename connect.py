import mysql.connector

try:
    cnx = mysql.connector.connect(user='', password='',
                              host='127.0.0.1',
                              database='3semi2024')
except mysql.connector.Error as err:
    print("Error: {}".format(err))
    exit()

print("MySQLに接続しました。")

cnx.close()