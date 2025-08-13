# PyCalculator!!!

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,}

def calculator():
    print('''
 _____________________
|  _________________  |
| |         GREY    | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
 ''')
    should_accumlate = True
    num1 = float(input("What if the first number : \n"))
    while should_accumlate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick and Operation : \n")
        num2 = float(input("What if the second number : \n"))

        answer = (operations[operation_symbol](num1, num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input("Type 'y' tp continue to continue with {answer}, or type 'n' to start over!\n").lower()

        if choice == "y":
            num1 = answer
        else:
            should_accumlate = False
            print("\n" * 100)
            calculator()

calculator()
