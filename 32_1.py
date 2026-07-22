# Write a program that creates a new text file every minute.The filename should contain the current timestamp.

import schedule
import time
import datetime

def CreateFile():
    filename = "File_" + datetime.now().strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    with open(filename, "w") as file:
        file.write("Filename : " + filename + "\n")
        file.write("Creation Date : " + datetime.now().strftime("%d-%m-%Y") + "\n")
        file.write("Creation Time : " + datetime.now().strftime("%I:%M:%S %p"))

    print(filename, "created successfully.")

schedule.every(1).minutes.do(CreateFile)

while True:
    schedule.run_pending()
    time.sleep(1)