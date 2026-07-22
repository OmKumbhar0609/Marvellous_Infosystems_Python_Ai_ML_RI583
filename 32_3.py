# Write a program that reads and displays the contents of a specified text file every minute.
# Handle the following conditions:
# File does not exist
# File is empty
# Permission is denied
# File cannot be opened

import schedule
import time

filename = input("Enter file name: ")

def ReadFile():
    try:
        with open(filename, "r") as file:
            data = file.read()

            if len(data.strip()) == 0:
                print("File is empty.")
            else:
                print("File Contents:")
                print(data)

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except Exception:
        print("File cannot be opened.")

schedule.every(1).minutes.do(ReadFile)

while True:
    schedule.run_pending()
    time.sleep(1)