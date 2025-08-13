# Hangman Word Game

import random

stages = [
'''
 +------+
 |      |
 |      |
(")     |
/|\     |
 |      |
/ \     |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
/|\     |
 |      |
/       |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
/|\     |
 |      |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
/|      |
 |      |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
 |      |
 |      |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
(")     |
        |
        |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''',
'''
 +------+
 |      |
 |      |
        |
        |
        |
        |
        |
        |
        |
  +-----+
  |     |
  +-----+
''']

word_list = ["dwarika","ayodhya","kailash","lanka","warrior"]

lives = 6

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      ''')

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    print(f"*********<{lives} LIVES LEFT!!!>*********")
    guess = input("Guess a letter : ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    display = ""
    
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "-"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, thats not in the word. You lose a life!")
        if lives == 0:
            game_over = True
            print("You Lose!")

    if "-" not in display:
        game_over = True
        print("You Win!")

    print(stages[lives])















