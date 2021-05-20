""" -Allow the player to submit a guess for a number between 1 and 100.
-Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
-If they got the answer correct, show the actual answer to the player.
-Track the number of turns remaining.
-If they run out of turns, provide feedback to the player. 
-Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode). """
import random
from random import randint

easy = 10 #if users choose the difficulty type as easy, they have 10 attems
hard = 5 #if users choose the difficulty type as hard, they have 5 attems
print("Welcome the Number Guessing Game ! ")
print( "I want you to keep a number in your mind between 1 and 100")    
def game():

    computer_number = random.randint(1,100)

    game_difficulty_type = input("Choose the difficulty type of game (easy or hard):\n").lower()

    if game_difficulty_type == 'easy':
        attempts = 10
    elif game_difficulty_type == 'hard':
        attempts =5
    else:
        print("you chose the WRONG difficulty type")

    while attempts > 0 :
        print(f"You have {attempts} remaining to guess the number.")
        guessed_num = int(input("Make a guess: "))
        if guessed_num > computer_number:
            print("Too high.")
        elif guessed_num < computer_number:
            print("Too low.")
        
        elif guessed_num == computer_number:
            print("Congratulations, you guessed the number!!!")
            break
        attempts -= 1

        if attempts == 0:
            print(f"You ran out of chances. The number was {computer_number}.")

        elif attempts > 0:
            print("Guess again.")

        


    
        
game()
