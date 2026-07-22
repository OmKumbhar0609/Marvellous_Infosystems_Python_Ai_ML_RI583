# Write a program which accepts two file names through command line arguments and compares the contents of both files.If both files contain the same contents, display Success,Otherwise display Failure

import sys

def CompareFiles(File1, File2):
    try:
        with open(File1, "r") as f1, open(File2, "r") as f2:

            if f1.read() == f2.read():
                print("Success")
            else:
                print("Failure")

    except FileNotFoundError:
        print("One or both files not found.")

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py File1 File2")
        return

    CompareFiles(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()