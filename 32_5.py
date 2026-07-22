# Write a program that deletes all empty files from a specified directory every hour.
# The program should:
# Scan the directory recursively
# Detect files whose size is zero bytes
# Delete the empty files
# Store deleted file paths in a log file
# Handle permission errors

import os
import schedule
import time
import datetime

directory = input("Enter directory path: ")

def DeleteEmptyFiles():
    with open("DeletedFilesLog.txt", "a") as log:

        for root, dirs, files in os.walk(directory):
            for file in files:

                filepath = os.path.join(root, file)

                try:
                    if os.path.getsize(filepath) == 0:
                        os.remove(filepath)

                        log.write(filepath + " deleted at " +
                                  datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")

                except PermissionError:
                    log.write("Permission denied : " + filepath + "\n")

                except Exception:
                    log.write("Error deleting : " + filepath + "\n")

    print("Empty file scan completed.")

schedule.every(1).hours.do(DeleteEmptyFiles)

while True:
    schedule.run_pending()
    time.sleep(1)