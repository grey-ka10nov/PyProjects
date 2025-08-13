# Treasure Island Choice Game

print ('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("Welsome to Treasure Island...")
print("Your Mission is to Find the Treasure...")
choice1 = input('You\'re at a Crossroad, Where do You Want to Go? Type "left" or "right"... ').lower()
if choice1 == "left":
    # Continue the Game
    choice2 = input('You have come to a lake.'
                    'This is an island in the middle of the lake.'
                    'Type "wait" to wait for a boat or "swim" to swim across.').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed."
                        "There is a house with 3 doors."
                        "Red, Yellow and Blue. Choose a door!").lower()
        if choice3 == "red":
            print("It's a room of flames... Game Over!!!")
        elif choice3 == "yellow":
            print("Congratulations, You found the Treasure...")
        elif choice3 == "blue":
            print("You unlocked the beasts that were trapped inside... Game Over!!!")
        else:
            print("No such choice exists. Game Over!!!")
    else:
        print('You were eaten by creatures of the sea...'
              'Game Over!!!')
if choice1 == "right":
    print("You fell into a hole! Game Over!!!")