from requests import get
from playsound import playsound
from os import remove
from threading import Thread
from time import sleep

def delamogus():
     sleep(1)
     remove("C:\\temp\\among_sus.mp3")

delete_amogus = Thread(target=delamogus)

url = 'https://cdn.discordapp.com/attachments/986817633661890580/1019756700389081098/among_sus.mp3'
r = get(url, allow_redirects=True)

open('C:\\temp\\among_sus.mp3', 'wb').write(r.content)
delete_amogus.start()
playsound("C:\\temp\\among_sus.mp3")