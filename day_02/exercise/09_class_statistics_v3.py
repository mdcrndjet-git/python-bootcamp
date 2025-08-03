from statistics import mean

student_scores = [98, 75, 100, 86, 100, 3]

# Print the average score
average_score = mean(student_scores)
print(f"Average score: {average_score}")

# Print the rankings, ascending or highest to lowest
print(f"Ascending order: {sorted(student_scores)}")

# Print the rankings, ascending or lowest to highest
print(f"Descending order: {sorted(student_scores, reverse = True)}")

