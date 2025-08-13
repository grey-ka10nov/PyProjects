# Rock, Paper n Scissor Game!!!

import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [Rock, Paper, Scissor]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 or Scissor : "))
print(game_images[user_choice])

comp_choice = random.randint(0, 2)
print(f"Computer chose : ")
print(game_images[comp_choice])

if user_choice>2 or user_choice<0:
    print("You typed an invalid number!")
elif user_choice == comp_choice:
    print("Its a draw!")
elif comp_choice == 0 and user_choice == 1:
    print("You Win!")
elif comp_choice == 1 and user_choice == 0:
    print("You lose!")
elif comp_choice == 1 and user_choice == 2:
    print("You Win!")
elif comp_choice == 2 and user_choice == 1:
    print("You lose!")
elif comp_choice == 2 and user_choice == 0:
    print("You Win!")
elif comp_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number!")
