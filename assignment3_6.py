# Write a program to display data type, memory address and size in bytes of a variable entered by the user.

x = input("Enter a value: ")
print("Data Type:", type(x))
print("Memory Address:", id(x))
print("Size in Bytes:", len(str(x)))

o/p: Enter a value: 27
Data Type: <class 'str'>
Memory Address: 2042335393376
Size in Bytes: 2
