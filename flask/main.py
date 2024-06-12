from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def top():
    return "Hello World!"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return render_template("hello.html", name="鷹野")

@app.route('/hellodb', methods=['GET', 'POST'])
def hellodb():
    # DB処理
    try:
        # ログイン
        cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='3semi2024')
        cur = cnx.cursor()
        print("MySQLに接続しました。")

        # SQLの定義
        sql = "SELECT student_id, name FROM student LIMIT 1"
        # SQLの実行
        cur.execute(sql)
        # 結果の取得
        for (student_id, name) in cur:
            print(student_id, name)
            myname = name
        print("SQLの実行に成功しました:" + sql)
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        #exit()
    
    cnx.close()
    
    return render_template("hello.html", name=myname)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)