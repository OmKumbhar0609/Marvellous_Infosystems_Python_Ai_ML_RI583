# Schedule a task that executes every five minutes,The task should write the current date and time into a file named:Marvellous.txt,New entries should be appended without removing previous entries.

import schedule
import time
from datetime import datetime

def WriteTime():
    with open("Marvellous.txt", "a") as file:
        now = datetime.now()
        file.write("Task executed at: ")
        file.write(now.strftime("%d-%m-%Y %I:%M:%S %p"))
        file.write("\n")

schedule.every(1).minutes.do(WriteTime)

while True:
    schedule.run_pending()
    time.sleep(1)