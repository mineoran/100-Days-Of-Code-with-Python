"""Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above.
 e.g. underweight, normal weight, overweight, obese, clinically obese. """


print("Welcome the Body Mass Index(BMI) calculator.")

user_weight = int(input("What is your weight: "))

user_height = float(input("Enter the your height: "))

BMI = (user_weight) / (user_height * user_height) 
BMI = round(BMI)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, isyou are underweight.")

elif BMI > 18.5 and BMI <25:
    print(f"Your BMI is {BMI}, you have a normal weight.")

elif BMI > 25 and BMI < 35:
    print(f"Your BMI is {BMI}, you are slightly overweight.")

elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI} , you are obese.")

else:
    print(f"Your BMI is {BMI}, you are clinically obese.")



