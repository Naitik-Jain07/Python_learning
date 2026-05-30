import random

choices = ["rock", "paper", "scissors"]   # list of options

user = input("Enter rock, paper, or scissors: ").lower()
computer = random.choice(choices)        # pick randomly from list

print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")