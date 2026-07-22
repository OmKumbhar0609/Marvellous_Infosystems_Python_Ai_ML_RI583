# Write a Python program that performs a file backup every hour,The program should:Accept the source file path,Accept the destination directory path,Copy the source file to the destination directory,Add the current date and time to the backup filename,Write the backup operation details into:backup_log.txt

import schedule
import time
import shutil
import os
import datetime

def Backup():
    source = input("Enter source file path: ")
    destination = input("Enter destination directory: ")

    if not os.path.exists(source):
        print("Source file not found.")
        return

    filename = os.path.basename(source)
    name, ext = os.path.splitext(filename)

    timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    newname = f"{name}_{timestamp}{ext}"

    destfile = os.path.join(destination, newname)

    shutil.copy(source, destfile)

    with open("backup_log.txt", "a") as log:
        log.write("Backup completed successfully at ")
        log.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
        log.write("\n")

    print("Backup Completed")

schedule.every().hour.do(Backup)

while True:
    schedule.run_pending()
    time.sleep(1)