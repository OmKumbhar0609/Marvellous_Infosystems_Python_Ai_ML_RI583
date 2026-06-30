# Write a program which accepts marks and displays grade.Conditions:Marks ≥ 75 → Distinction,Marks ≥ 60 → First Class,Marks ≥ 50 → Second Class,Marks < 50 → Fail

marks = float(input("Enter the marks: "))

if marks >= 75:
    print("Grade: Distinction")
elif marks >= 60:
    print("Grade: First Class")
elif marks >= 50:
    print("Grade: Second Class")
else:
    print("Grade: Fail")