student_scores = input("Input a list of student scores : ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
print(student_scores)

highscore = student_scores[0]

for i in range(1, len(student_scores)):
    if highscore < student_scores[i]:
        highscore = student_scores[i]
        
print(f"The highest score is : {highscore}")

