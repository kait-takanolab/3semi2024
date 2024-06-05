import mysql.connector

cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='3semi2024')

print("MySQLに接続しました。")

cnx.close()