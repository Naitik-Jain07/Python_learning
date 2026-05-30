import random
correct_num = random.randint(1,100)
print (correct_num)
chance = 0

def level():
    global diff_level , chance
    diff_level = input(str("Enter difficulty level: easy or hard")).lower()
    if diff_level == "easy":
        chance = 10
        print("you have 10 chances")
    elif diff_level == "hard":
        chance = 5
        print("you have 5 chances")
    else:
        print("type easy or hard")

def chance_calc():
    global chance
    chance = chance - 1

def game_over_check():
    global game_over
    if chance == 0:
        print ('GAME OVER LIL BUDDY')
        game_over = True

    else:
        print('WRONG GUESS . TRY AGAIN LIL BUDDY')
        game()

def game():
    global guessed_num
    guessed_num = int(input("Whats ur guessed num: \n"))
    if guessed_num > correct_num:
        print('TOO HIGH')
        chance_calc()
        game_over_check()
    elif guessed_num < correct_num:
        print("TOO LOW")
        chance_calc()
        game_over_check()


game_over = False
while not game_over:
    level()
    game()
    if game_over:
        replay = input('wanna play again?: y or n: \n')
        if replay != 'y':
            game_over
        else :
            not game_over

        






        

