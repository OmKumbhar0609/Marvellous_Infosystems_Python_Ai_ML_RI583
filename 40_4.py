# Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Display predictions clearly.

from pyexpat import model
from turtle import pd


new_students = pd.DataFrame({

"StudyHours":[6,4,8,2,7],
"Attendance":[85,65,95,50,90],
"PreviousScore":[66,55,90,40,80],
"AssignmentsCompleted":[7,4,10,2,8],
"SleepHours":[7,6,8,5,7]

})

prediction = model.predict(new_students)

new_students["Prediction"] = prediction

print(new_students)