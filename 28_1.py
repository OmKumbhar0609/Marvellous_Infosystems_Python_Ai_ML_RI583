# Write a program which accepts a file name from the user and counts how many lines are present in the file.

def CountLines(FileName):
    try:
        with open(FileName, "r") as file:
            count = 0
            for line in file:
                count = count + 1
        print("Total number of lines:", count)

    except FileNotFoundError:
        print("File not found.")

def main():
    Name = input("Enter file name: ")
    CountLines(Name)

if __name__ == "__main__":
    main()