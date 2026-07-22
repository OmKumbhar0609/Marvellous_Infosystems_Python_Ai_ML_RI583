# Write a program that scans a specified directory every minute,The task should display:Directory name,Number of files,Number of subdirectories,Date and time of scanning,Use the os module.

import os
import schedule
import time
import datetime

directory = input("Enter directory path: ")

# Validate directory path
if not os.path.exists(directory):
    print("Error: Directory does not exist!")
    exit()

def ScanDirectory():
    files = 0
    folders = 0

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        if os.path.isfile(path):
            files = files + 1
        elif os.path.isdir(path):
            folders = folders + 1

    print("Directory Scanned:", directory)
    print("Total Files:", files)
    print("Total Subdirectories:", folders)
    print("Scan Time:", datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print()

schedule.every(1).minutes.do(ScanDirectory)

while True:
    schedule.run_pending()
    time.sleep(1)