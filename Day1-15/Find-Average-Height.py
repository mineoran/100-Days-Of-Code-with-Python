"""  You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
The average height can be calculated by adding all the heights together and 
dividing by the total number of heights.  """

student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0

for height in student_heights :
    total_height += height
print(f"total height = {total_height}")

number_of_student = 0

for student in student_heights:
    number_of_student += 1
print(f"number of students = {number_of_student}")

average_height = round(total_height / number_of_student)
print(average_height)
