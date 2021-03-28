import random

user_choice = int(input("Choice 1 for Head or 0 for Tail: "))
random_toss = random.randint(0,1)

if random_toss == 1:
    print("Heads")
else:
    print("Tails")


