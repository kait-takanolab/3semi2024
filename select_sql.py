import mysql.connector

try:
    cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='3semi2024')
    cur = cnx.cursor()

    print("MySQLに接続しました。")

    # sql
    sql = "SELECT student_id, name FROM student"
    cur.execute(sql)
    #cnx.commit()

    for (student_id, name) in cur:
        print(student_id, name)
    print("SQLの実行に成功しました:" + sql)
except mysql.connector.Error as err:
    print("Error: {}".format(err))
    exit()
    
cnx.close()