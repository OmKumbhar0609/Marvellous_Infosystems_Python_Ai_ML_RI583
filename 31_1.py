# Write a program that accepts:A message from the user,A time interval in seconds,Schedule the program to display the message repeatedly after the specified interval.

import schedule
import time

def Display(msg):
    print(msg)

message = input("Enter message: ")
interval = int(input("Enter interval in seconds: "))

if interval <= 0:
    print("Interval must be greater than zero.")
else:
    schedule.every(interval).seconds.do(Display, message)

    while True:
        schedule.run_pending()
        time.sleep(1)