# Caesar PyCipher

print('''
   _____                             _____        _____ _       _               
  / ____|                           |  __ \      / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __  | |__) |   _| |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| |  ___/ | | | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | |   | |_| | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|    |_|    \__, |\_____|_| .__/|_| |_|\___|_|   
                                            __/ |        | |                    
                                           |___/         |_|  ''')


charac = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
                shift_amount *= -1
                
    for letter in original_text:

        if letter not in charac:
            output_text += letter
        else:
            shifted_position = charac.index(letter) + shift_amount
            shifted_position %= len(charac)
            output_text += charac[shifted_position]
    print(f"Here is the {encode_or_decode}d result : \n{output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, tyoe 'decode' to decrypt : \n").lower()
    text = input("Type your message : \n").lower()
    shift = int(input("Type the shift number : \n"))

    caesar(original_text = text, shift_amount = shift, encode_or_decode = direction)

    restart = input("Type 'yes' if you want to go again, Otherwise tupe 'no' : \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
