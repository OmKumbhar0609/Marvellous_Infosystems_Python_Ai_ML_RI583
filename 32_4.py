# Write a program that copies all .txt files from one directory to another every ten minutes.
# The program should:
# Accept source and destination directories
# Validate both directories
# Copy only .txt files
# Maintain a log of copied files
# Avoid terminating if one file cannot be copied

import os
import shutil
import schedule
import time
import datetime

source = input("Enter source directory: ")
destination = input("Enter destination directory: ")

def CopyFiles():
    if not os.path.isdir(source) or not os.path.isdir(destination):
        print("Invalid directory.")
        return

    with open("CopyLog.txt", "a") as log:
        for file in os.listdir(source):
            if file.endswith(".txt"):
                src = os.path.join(source, file)
                dst = os.path.join(destination, file)

                try:
                    shutil.copy2(src, dst)
                    log.write(file + " copied at " +
                              datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
                except Exception:
                    log.write(file + " could not be copied.\n")

    print("Copy operation completed.")

schedule.every(10).minutes.do(CopyFiles)

while True:
    schedule.run_pending()
    time.sleep(1)