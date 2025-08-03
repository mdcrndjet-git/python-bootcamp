student_names = ("Juan","Maria","Joseph")
student_scores = (70, 90, 81)

"""
Print the student scores and names in  the following format
Student Records:
    Student: Juan scored 70 in the exam.
    Student: Maria scored 90 in the exam.
    Student: Joseph scored 81 in the exam.
    
    Print the student that got the highest score.
"""

for student_name, student_score in zip(student_names, student_scores):
    print(f"Student: {student_name} scored {student_score} in the exam.")

highest_score = max(student_scores)
for student_name, student_score in zip(student_names, student_scores):
    if student_score == highest_score:
        print(f"Student: {student_name} got the highest score in the exam.")
        