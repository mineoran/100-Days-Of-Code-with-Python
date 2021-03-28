"""   Write a program that adds the digits in a 2 digit number. 
e.g. if the input was 35, then the output should be 3 + 5 = 8
Warning: Do not change the code on lines 1-3. Your program should work for different inputs. 
e.g. any two-digit number.     """

number = input("Enter two-digit number: ")
print(int(number[0]) + int(number[1]))


"""  Attention Please!

print(number[0] + number[1])  
When I write it as print (number [0] + number [1]), the code output does not change, 
because the input value is string data type.
That's why we need to convert our number index values to integers. """