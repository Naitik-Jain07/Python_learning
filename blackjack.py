import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user = []
computer = []
user_score = 0
computer_score = 0
game_over = False

def ace():
    global game_over, user_score, computer_score

    if computer_score > 21:
        for value in computer:
            if value == 11:
                computer_score -= 10
                break
        else:
            print("PLAYER WINS")
            game_over = True

    if user_score > 21:
        for value in user:
            if value == 11:
                user_score -= 10
                break
        else:
            print("COMP WINS")
            game_over = True

# Deal initial hand ONCE, before the loop
for i in range(2):
    user.append(random.choice(cards))
    computer.append(random.choice(cards))

for card in user:
    user_score += card
for card in computer:
    computer_score += card

print("Your hand:", user)

while not game_over:
    if computer_score == user_score:
        print("TIE")
        game_over = True
    elif computer_score > user_score:
        if computer_score > 21:
            ace()
        else:
            print("COMPUTER WINS")
            game_over = True
    elif user_score > computer_score:
        if user_score > 21:
            ace()
        else:
            print("PLAYER WINS")
            game_over = True