# Based on the dataset values, analyze whether:
# Higher StudyHours increase the chance of passing.
# Higher Attendance improves FinalResult.


from turtle import pd

df = pd.read_csv("student_performance_ml.csv")

# Analyze the relationship between StudyHours and FinalResult
study_hours_pass = df[df["FinalResult"] == 1]["StudyHours"].mean()
study_hours_fail = df[df["FinalResult"] == 0]["StudyHours"].mean()

print("Average Study Hours for Passed Students:", study_hours_pass)
print("Average Study Hours for Failed Students:", study_hours_fail)

# Analyze the relationship between Attendance and FinalResult
attendance_pass = df[df["FinalResult"] == 1]["Attendance"].mean()
attendance_fail = df[df["FinalResult"] == 0]["Attendance"].mean()

print("Average Attendance for Passed Students:", attendance_pass)
print("Average Attendance for Failed Students:", attendance_fail)