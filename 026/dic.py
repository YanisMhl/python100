import random 
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {name:random.randint(1, 100) for name in names}

print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}


print(passed_students)