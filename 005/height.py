heights = input("Give me the heights of students in cm seperated by columns")

student_heights = heights.split(",")

sum = 0
for student in student_heights:
    sum += int(student)

sum /= len(student_heights)

print(f"The average height of the class is {sum}cm ({len(student_heights)} students)")