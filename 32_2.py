# Write a Python program that monitors the size of a specified file every 30 seconds.Handle the situation where the file does not exist.

import os
import schedule
import time
import datetime

filepath = input("Enter file path: ")

def MonitorFile():
    with open("FileSizeLog.txt", "a") as log:
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            log.write("File : " + filepath + "\n")
            log.write("Size : " + str(size) + " bytes\n")
            log.write("Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
            log.write("---------------------------------\n")
            print("File size logged.")
        else:
            log.write("File not found : " + filepath + "\n")
            log.write("Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
            log.write("---------------------------------\n")
            print("File does not exist.")

schedule.every(30).seconds.do(MonitorFile)

while True:
    schedule.run_pending()
    time.sleep(1)