# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.

def DisplayFile(FileName):
    try:
        with open(FileName, "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("File not found.")

def main():
    Name = input("Enter file name: ")
    DisplayFile(Name)

if __name__ == "__main__":
    main()