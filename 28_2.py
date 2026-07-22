# Write a program which accepts a file name from the user and counts the total number of words in that file.

def CountWords(FileName):
    try:
        with open(FileName, "r") as file:
            data = file.read()
            words = data.split()
            print("Total number of words:", len(words))

    except FileNotFoundError:
        print("File not found.")

def main():
    Name = input("Enter file name: ")
    CountWords(Name)

if __name__ == "__main__":
    main()