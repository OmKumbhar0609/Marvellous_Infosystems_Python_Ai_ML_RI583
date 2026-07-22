# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.

import os

def CheckFile(FileName):
    if os.path.exists(FileName):
        print("File exists.")
    else:
        print("File does not exist.")

def main():
    Name = input("Enter file name: ")
    CheckFile(Name)

if __name__ == "__main__":
    main()