# Guess the number!!!

print('''
   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
''')

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_guess, turns):
    """Checks answer against guess, retunrs the number of turns remaining!!!"""
    if user_guess > actual_guess:
        print("Too High!")
        return turns - 1
    elif user_guess < actual_guess:
        print("Too Low!")
        return turns - 1
    else:
        print("You got it! The answer was {actual_answer}")

def set_difficulty():
    level = input("Choose a difficulty, type 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100...\n")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0 
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number!")

        guess = int(input("Make a guess : \n"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess Again!")

game()