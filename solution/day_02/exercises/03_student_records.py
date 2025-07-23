student_names = ("Juan", "Maria", "Joseph")
student_scores = (70, 90, 81)

"""
Print the student scores and names in the following format
Student Records:
Student: Juan scored 70 in the exam.
	Student: Maria scored 90 in the exam.
	Student: Joseph scored 81 in the exam.
"""

highest_score = student_scores[0]
highest_name = student_names[0]
for name, score in zip(student_names, student_scores):
    print(f"Student: {name} scored {score} in the exam")

    if score > highest_score:
        highest_score = score
        highest_name = name

print("Highest score:", highest_score, "from", highest_name)
