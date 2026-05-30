import logo_art
print(logo_art.logo)

continue_bid = 'True' 
dictionary = {}

while continue_bid == 'True':
    name = input(str("Whats your name: \n"))
    bid = input("Enter your bid")
    
    dictionary[name] = int(bid)
    

    max_bid = 0
    winner = ''
    
    for name,bid in dictionary.items():
        if int(bid) >= max_bid:
            max_bid = int(bid)
            winner = name

    print(max_bid)
    continue_bid = str(input("any other bet?: yes or no")).lower()
    if (continue_bid == "yes"):
        continue_bid = 'True'
        print('\n' * 100)

    elif (continue_bid == 'no'):
        continue_bid = 'False'
        print("Winner of the auction is " +winner +" with bid of " + str(max_bid) )   

    else:
        print("yes or no only") 
          

 
    
   
        
