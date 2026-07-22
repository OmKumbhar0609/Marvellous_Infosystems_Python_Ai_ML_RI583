# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.

def CountFrequency(FileName, Word):
    try:
        with open(FileName, "r") as file:
            data = file.read()

        words = data.split()
        count = words.count(Word)

        print("Frequency of", Word, "is:", count)

    except FileNotFoundError:
        print("File not found.")

def main():
    Name = input("Enter file name: ")
    Word = input("Enter word: ")

    CountFrequency(Name, Word)

if __name__ == "__main__":
    main()