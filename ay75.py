import random
#imcomplete

#TODO 1 UPDATE WORD LIST TO "WORD_LIST" FROM HANGMAN_WORDS.PY
import hangman_words
import hangman_art

print(hangman_art.art)

stages = [
    """ 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
    """ 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """ 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """ 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """ 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """ 
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """ 
  +---+
  |   |
      |
      |
      |
      |
========="""
]
words=hangman_words.word_list


lives = 6
#TODO 2 IMPORT LOGO FROM HANGMAN_ART.PY AND PRINT IT AT START OF GAME
word= random.choice(words)
print(word)

placeholder = ''
for a in range(len(word)):
    x = '_'
    placeholder += x
print(placeholder)

game_over = False
correct_letter=[]
while not game_over:
    #TODO 4 UPDATE CODE BELOW TO TELLL USER HOW MANY LIFES ARE LEFT NOW
    guess=input("Guess a letter in lowercase").lower()


    display=''

   
    for letter in word:
    
        if letter== guess:
            display+= letter
            correct_letter.append(guess)
        
        elif letter in correct_letter:
            display+=letter
            
        else:
            display+= "_"
            
    print(display)

   
    if guess not in word:
        lives = lives - 1 
        if lives==0:
            print("u lost")
            game_over = True

    if "_" not in display:
        game_over= True
        print("You Win")

    print (f"remaining lives: {lives}")
    print(stages[lives])