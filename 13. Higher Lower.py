# Higher Lower!!!

logo = """
 __    __   __    _______  __    __   _______  ______      
|  |  |  | |  |  /  _____||  |  |  | |   ____||   _  \     
|  |__|  | |  | |  |  __  |  |__|  | |  |__   |  |_)  |    
|   __   | |  | |  | |_ | |   __   | |   __|  |      /     
|  |  |  | |  | |  |__| | |  |  |  | |  |____ |  |\  \----.
|__|  |__| |__|  \______| |__|  |__| |_______|| _| `._____|
 __        ______   ____    __    ____  _______  ______      
|  |      /  __  \  \   \  /  \  /   / |   ____||   _  \     
|  |     |  |  |  |  \   \/    \/   /  |  |__   |  |_)  |    
|  |     |  |  |  |   \            /   |   __|  |      /     
|  `----.|  `--'  |    \    /\    /    |  |____ |  |\  \----.
|_______| \______/      \__/  \__/     |_______|| _| `._____|"""

vs = """
____    ____     _______    
\   \  /   /    /       |    
 \   \/   /    |   (----`    
  \      /      \   \        
   \    / __.----)   |    __ 
    \__/ (__)_______/    (__)"""

data = [
    {
        'name' : 'Salman Khan',
        'follower_count' : 70.8,
        'description' : 'Actor',
        'country' : 'India'
    },
    {
        'name' : 'Shahrukh Khan',
        'follower_count' : 48.2,
        'description' : 'Actor',
        'country' : 'India'
    },
    {
        'name' : 'Amitabh Bachchan',
        'follower_count' : 37.3,
        'description' : 'Actor',
        'country' : 'India'
    },
    {
        'name' : 'Virat Kohli',
        'follower_count' : 273.6,
        'description' : 'Crickter',
        'country' : 'India'
    },
    {
        'name' : 'Rohit Sharma',
        'follower_count' : 44,
        'description' : 'Cricketer',
        'country' : 'India'
    },
    {
        'name' : 'Honey Singh',
        'follower_count' : 19.5,
        'description' : 'Singer',
        'country' : 'India'
    },
    {
        'name' : 'Talwinder Singh Sidhu',
        'follower_count' : 1.4,
        'description' : 'Singer',
        'country' : 'India'
    },
    {
        'name' : 'Karan Aujla',
        'follower_count' : 10.1,
        'description' : 'Singer',
        'country' : 'India'
    },
    {
        'name' : 'Prabhas Raju',
        'follower_count' : 13.2,
        'description' : 'Actor',
        'country' : 'India'
    },
    {
        'name' : 'Deepika Padukone',
        'follower_count' : 80,
        'description' : 'Actor',
        'country' : 'India'
    },
    {
        'name' : 'Shraddha Kapoor',
        'follower_count' : 94,
        'description' : 'Actor',
        'country' : 'India'
    },
]

import random

def format_data(account):
    #Takes the account data and returns the printable format...
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    #Takes a user's guess and the follower counts and returns if they got it right...
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}!")
    print(vs)
    print(f"Against B : {format_data(account_b)}!")

    guess = input("WHo had more followers? Type 'A' or 'B' : \n").lower()

    print("\n" * 50)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, thats wrong! Final score : {score}")
        game_should_continue = False