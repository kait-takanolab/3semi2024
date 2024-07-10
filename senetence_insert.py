from gtts import gTTS
import os
import mysql.connector

AUDIO_FOLDER = "audio"

# DB接続
try:
    cnx = mysql.connector.connect(user='', password='',
                              host='',
                              database='')
    cur = cnx.cursor()

    print("MySQLに接続しました。")
except mysql.connector.Error as err:
    print("Error: {}".format(err))
    exit()



# ファイルオープン
with open('en_text.txt') as f:
    lines = f.readlines()

allline = "".join(lines)

# ピリオド分割して、1文ずつを取り出す
# 1文ずつ配列linesに格納する

print (allline)
lines = allline.split('.')

topic_id = 1

length = len(lines)
print (lines, length)
for i, line in enumerate(lines):
    line.replace('\n', '')
    print(line)
    if line == '':
        continue

    # オーディオファイル名(IDと兼用)を生成
    # トピックID_英文ID.mp3
    file_name = str(topic_id) + "_" + str (i+1) + ".mp3"
    # ファイルパスを生成
    audio_path = os.path.join(AUDIO_FOLDER, file_name)
    print(audio_path)

    # 1文をDBに格納 (英文ID - 数字の連番)
    # ファイルパスをDBに格納
    try:
        # sql
        # sql = "INSERT INTO sentence (id, topic_id, sentence, audio_path) VALUES (" + str(i+1) +"," + str(topic_id) + ",'" + line + "','" + audio_path + "');"
        sql = "INSERT INTO sentence (id, topic_id, sentence, audio_path) VALUES (%s, %s, %s, %s);"
        data_sentence = (str(i+1), str(topic_id), line, audio_path)
        print(sql)
        cur.execute(sql, data_sentence)
        cnx.commit()

        print("SQLの実行に成功しました:" + sql)
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        exit()



    tts = gTTS(text=line, lang='en')
    file_name = str(topic_id) + "_" + str(i+1) + ".mp3"
    tts.save(os.path.join("audio", file_name))

cnx.close()