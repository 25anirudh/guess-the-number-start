
from art import logo
print(logo)
import random
easy_level_turns = 10
hard_level_turns = 5

def check_answer(guess, actual, turn):
  if guess > actual:
    print("your guess is very high")
    return turn -1 
  elif guess < actual:
    print("your guess is very low")
    return turn -1
  else :
    print("you guessed the correct number , you won")
def set_difficulty():
  level = input("choose the difficulty level 'easy' or 'hard' : ")
  if level == "easy":
    return easy_level_turns
  else:
    return hard_level_turns
def game():
  print("wlcm to the number guessing game , I am thinking of a number between 1-100")
  actual = random.randint(0,100)
  turn = set_difficulty()
  guess = 0
  while guess != actual :
    print(f"you have {turn} attempts remaining to guess the number  ")
    guess = int(input("make a guess:"))
    
    turn = check_answer(guess , actual,turn)
    if turn == 0:
      print("you've run out of guesses you loose")
      return
    elif guess != actual:
      print("guess again")

game()
