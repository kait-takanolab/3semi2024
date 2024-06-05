import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='3semi2024')
    cur = cnx.cursor()

    print("MySQLに接続しました。")

    # sql
    sql = "INSERT INTO student (student_id, name) VALUES ('2221200', '厚木たろう');"
    cur.execute(sql)
    cnx.commit()

    print("SQLの実行に成功しました:" + sql)
except mysql.connector.Error as err:
    print("Error: {}".format(err))
    exit()





cnx.close()