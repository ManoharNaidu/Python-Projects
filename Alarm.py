import time
from plyer import notification
import os

def sec(h,m,s):
    return h*3600 + m*60 + s

user_time = input("Set Alarm(in hh/mm/ss): ")

hour ,minute , second = user_time.split("/")
t = sec(int(hour),int(minute),int(second))

while t+1:
    h = t//3600
    m = t//60 - h*60
    s = t%3600 - m*60
    timer = "{:02d}:{:02d}:{:02d}".format(h,m,s)
    print(" " + timer, end = "\r")
    time.sleep(1)
    t -= 1

title = "Alarm Alert!"
message = "Set alarm out of time..."

notification.notify(title = title,
                    message = message,
                    app_icon = os.path.join("clock.ico"), #add your icon
                    timeout = 5,
                    toast = False)
quit()