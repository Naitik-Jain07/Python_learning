caesar_cipher_art = """
   _____                              _____ _       _               
  / ____|                            / ____(_)     | |              
 | |     __ _  ___  ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
 | |___| (_| |  __/\__ \ (_| | |    | |____| | |_) | | | |  __/ |   
  \_____\__,_|\___||___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                             | |                    
                                             |_|                    
"""
print(caesar_cipher_art)

# TODO1: IF SYMBOL IS THERE IN TEXT HOW ARE U GONNA KEEP IT IN ENCODED OR DECODED TEXT

def caesar (original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        # TODO1
        if letter not in alphabets:
            output_text=+letter

        else :
             
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets [shifted_position]

    print(f"Here is the encoded result: {output_text}")

#TODO2: H0OW MAKE CODE KEEP RUNNING UNTIL USER ASKES TO
should_continue = 'true'
while should_continue :
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = str(input ("type 'encode' to encrypt and type 'decode' to decrypt: \n").lower())
    text = input("Type ur message : \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar (original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart= input("wanna continue?yes or no").lower()
    if restart == "no":
        should_continue= 'false'
        print('goodbye')

    elif restart == 'yes':
        should_continue = 'true'
