print(''' 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
                                                                 ''')

print('WELCOME TO TREASURE ISLAND')
move = str(input("Ur next move : l for left and r for right"))

if (move== "l"):
    move2 = str(input('CONGRATS. U PASSED LEVEL 1. \n now,how do u wanna cross river? S for swim and W for wait for boat'))
    if (move2== "w"):
        print("CONGRATS . U PASSED LEVEL 2. \n KEEP GOING CHAMP")
        move3=str(input("There are 3 doors.  \nwhich door will u choose?B for blue, r for red and y for yellow"))
        if(move3=="r"):
            print("U GOT BURNED. \n GAME OVER")
        elif(move3=="b"):
            print("U GOT EATEN BY BEASY.  \nGAME OVER")
        elif(move3=="y"):
            print("CONGRATS CHAMPION")
        else:
            print("GAME OVER")
    else:
        print("LOOTERS ATTACKED U.  \nGAME OVER")
else:
    print("U FELL INTO HOLE.  \nGAME OVER")