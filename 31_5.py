# Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes.Write the result into:DirectoryCountLog.txt,Each entry should contain:,Directory path,Number of files,Date and time

import os
import schedule
import time
from datetime import datetime

directory = input("Enter directory path: ")

def CountFiles():
    count = 0

    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            count += 1

    with open("DirectoryCountLog.txt", "a") as file:
        file.write("Directory : " + directory + "\n")
        file.write("Files : " + str(count) + "\n")
        file.write("Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
        file.write("----------------------------------\n")

    print("Log Updated")

schedule.every(5).minutes.do(CountFiles)

while True:
    schedule.run_pending()
    time.sleep(1)