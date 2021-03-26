#Day 2.2 BMI Calculator
"""   Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some's weight taking into account their height. 
e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):  """

person_weight = int(input("Enter the weight: "))

person_height = float(input("Enter the height: "))

person_BMI = (person_weight / (person_height*person_height))

print(person_BMI)

