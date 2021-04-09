print("Welcome to Python Pizza Deliveries!")

size = input("How would you like the pizza size? S, M or L \n")

pepperoni = input("Do you want pepperoni ? Y or N \n")

Extra_chesse = input("Do you want extra chesse? Y or N \n")

total_bill = 0
if size == "S":
    total_bill += 15

elif size == "M":
    total_bill += 20
else:
    total_bill += 25

if pepperoni == "Y":
    if size == "S" :
        total_bill += 2
    else:
        total_bill +=3
    
if Extra_chesse == "Y":
    total_bill += 1

print(f"Your total bill is : $ {total_bill}.")
