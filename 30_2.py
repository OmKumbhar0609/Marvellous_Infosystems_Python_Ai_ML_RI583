# Write a Python program that displays the current date and time after every one minute.Use the datetime module.

import schedule
import time
import datetime

def display():
    print("Current date and time is:",datetime.datetime.now())

schedule.every(1).minutes.do(display)

while True:
    schedule.run_pending()
    time.sleep(1)