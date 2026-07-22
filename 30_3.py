# Write a program that schedules a function to print:Coding Kar... for every 30 minutes.

import schedule
import time

def Display():
    print("Coding kar...")

def main():
    print("Automation script started")
    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()