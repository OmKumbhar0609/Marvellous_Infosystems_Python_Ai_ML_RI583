# Write a Python program that prints:Jay Ganesh...every two seconds .

import schedule
import time
import datetime

def Display():
    print("Jay Ganesh...")
schedule.every(2).seconds.do(Display)

while True:
    schedule.run_pending()
time.sleep(1)

