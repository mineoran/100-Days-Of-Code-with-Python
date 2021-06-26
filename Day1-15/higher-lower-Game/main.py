from game_data import data
from art import logo, vs
import os 
import random
# Generate a random account from the game data.


def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(user_guess, first_followers, second_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if first_followers > second_followers:
    return user_guess == "a"
  else:
    return user_guess == "b"

def game():
    score=0
    print(logo)
    first_account = random.choice(data)
    second_account = random.choice(data)
    while first_account == second_account:
        second_account = random.choice(data) 
    print(f"Compare A: {format_data(first_account)}.")
    print(vs)
    print(f"Against B: {format_data(second_account)}.")
    user_guess = input("Who has more followers? Type 'A' or 'B' :").lower()
    first_account_count = first_account["follower_count"]
    second_account_count = second_account["follower_count"]

    is_correct = check_answer(user_guess,first_account_count,second_account_count)
    os.system('cls')
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()







# Check if user is correct.
## Get follower count.
## If Statement

# Feedback.


# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.