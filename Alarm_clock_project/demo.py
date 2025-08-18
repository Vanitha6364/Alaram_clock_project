from tkinter.ttk import *
from tkinter import *

from datetime import datetime
from time import sleep


from pygame import mixer
window = Tk()
window.title("")
window.geometry('350x150')


def sound_alarm():
    mixer.music.load('alarm3.mp3')
    mixer.music.play()

def alarm():
    while True:
     control=1
     print(control)
     alarm_hour='17'
     alarm_minute='20'
     alarm_secomd='00'
     alarm_period='PM'.upper()

     now=datetime.now()
     hour=now.strftime("%I")
     minute=now.strftime("%M")
     second=now.strftime("%S")
     period=now.strftime("%p")


     if control==1:
        if alarm_period==period:
           if alarm_hour==hour:
              if alarm_minute==minute:
                 if alarm_secomd==second:
                    print("Time to take a break!")
                    sound_alarm()
    sleep(1)

mixer.init()
alarm()

window.mainloop()
#c:\Users\vanit\Downloads\alarm3.wav
