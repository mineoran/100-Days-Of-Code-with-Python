#You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions.
# The output words must match the example. i.e .The highest score in the class is: x

student_scores = input("Enter the student scores:").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

high_score = 0
for  score in student_scores:
    if score > high_score:
        high_score = score

print(f"The highest score in the class is : {high_score}")


