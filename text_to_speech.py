from gtts import gTTS
import os

with open('en_text.txt') as f:
    lines = f.readlines()

print (lines)
#for i, line in enumerate(lines):
#    line.replace('\n', '')
#    print(line)

line = lines
#line = "Hello, Sato-san."
i = 0

tts = gTTS(text=line, lang='en')
file_name = str(i) + ".mp3"
tts.save(os.path.join("audio", file_name))