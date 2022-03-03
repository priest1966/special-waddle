import datetime
import time


def hello_world(tts):
    print(__main__)
    print(datetime.datetime.now())
    print("~ sleeping for " + str(tts))
    time.sleep(tts)


hello_world(2)
from os import system
system("bash execute_my_app.sh")
