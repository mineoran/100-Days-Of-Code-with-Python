#Write a program that works out whether if a given year is a leap year. 
#A normal year has 365 days, leap years have 366, with an extra day in February.
# On every year that is evenly divisible by 4 **except** every year 
# that is evenly divisible by 100 **unless** the year is also evenly divisible by 400


leap_year = int(input("Enter the year: "))
if leap_year % 4 == 0:
  if leap_year % 100 == 0:
    if leap_year % 400 == 0:
      print("The year you entered is leap year.")
    else:
      print("Not leap year.")
  else:
    print("The year you entered is leap year.")
else:
  print("Not leap year.")