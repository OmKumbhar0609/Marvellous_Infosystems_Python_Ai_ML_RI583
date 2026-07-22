# Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.

def DisplayFile(FileName):
    try:
        with open(FileName, "r") as file:
            for line in file:
                print(line, end="")

    except FileNotFoundError:
        print("File not found.")

def main():
    Name = input("Enter file name: ")
    DisplayFile(Name)

if __name__ == "__main__":
    main()