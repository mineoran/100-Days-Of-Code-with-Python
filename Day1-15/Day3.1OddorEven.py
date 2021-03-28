#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder.

user_number = int(input("Enter number to check:"))

if user_number % 2 == 0:
    print("The number you entered is even. \n")

else:
    print("The number you entered is odd. \n")


