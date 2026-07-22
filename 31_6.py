# Write a program that schedules the following messages:Monday at 9:00 AM: Start your weekly goals,Wednesday at 5:00 PM: Review your weekly progress,Friday at 6:00 PM: Weekly work completed

import schedule
import time

def MondayTask():
    print("Start your weekly goals")

def WednesdayTask():
    print("Review your weekly progress")

def FridayTask():
    print("Weekly work completed")

schedule.every().monday.at("09:00").do(MondayTask)
schedule.every().wednesday.at("17:00").do(WednesdayTask)
schedule.every().friday.at("18:00").do(FridayTask)

while True:
    schedule.run_pending()
    time.sleep(1)