"""Create a program using maths and 
f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. """

user_time = int(input("Enter the your age:"))

years = 90 - user_time

remaining_day = years * 365
remaining_week = years * 52
remaining_months = years * 12 

print(f"You have {remaining_day} days, {remaining_week} weeks and {remaining_months} months left.")

