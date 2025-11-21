import random 
comp = random.randint(1, 6)
while True:
    user_input = input('Chosse a number from 1 to  6 or type quit to exit: ')
    if user_input.lower() == "quit":
        print("Bye!!")
        break 
    try:
        choice= int(user_input)
        
        if choice == comp :
            print("You win") 
        elif choice > comp :
            print("number is too high!!")   
        elif choice < comp :
            print("number too low")  
        
    except ValueError :
        print("Error!! invalid input")          
