# Write a program which accepts one character and checks whether it is vowel or consonant.

char = input("Enter a character: ")
if char in 'aeiouAEIOU':
    print("It is a vowel.")
else:
    print("It is a consonant.")