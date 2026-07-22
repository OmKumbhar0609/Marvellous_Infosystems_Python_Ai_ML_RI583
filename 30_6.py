# Write a script that schedules the following tasks:Print Lunch Time! every day at 1:00 PM.Print Wrap up work every day at 6:00 PM.Both tasks should be handled by separate functions.

import schedule
import time

def Lunch():
    print("Lunch Time!")

def WrapUp():
    print("Wrap up work")

schedule.every().day.at("13:00").do(Lunch)
schedule.every().day.at("18:00").do(WrapUp)

while True:
    schedule.run_pending()
    time.sleep(1)