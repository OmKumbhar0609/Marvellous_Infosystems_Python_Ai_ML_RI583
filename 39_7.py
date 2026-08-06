# Predict result for a student having:
# StudyHours = 6
# Attendance = 85
# PreviousScore = 66
# AssignmentsCompleted = 7
# SleepHours = 7

from xml.parsers.expat import model

student = [[6, 85, 66, 7, 7]]

prediction = model.predict(student)

if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")