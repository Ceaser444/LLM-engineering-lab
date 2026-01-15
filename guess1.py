import random 

total_guess =0
wins = 0
loss = 0

all_guess = []#total guess of a player 
guess_frequency = {}#this tracks how many times a number was guessed

while True:
    print("OLS GUESSING GAME")
    print("\n1.Play game")
    print("2.View stats")
    print("3.Exit")
    
    user = input("\nSelect a menu:")
    if user == "1":
        secret_num = random.randint(1, 10)
        attempts= 4
        win = False
        
        total_guess += 1
        
        print("\nAm thinking of a number between 1 to 10")
        print("You have 4 attempts to guess the right num")
        
        while attempts > 0:
            guess = int(input("what num is on my mind: "))
            
            all_guess.append(guess)
            if guess in guess_frequency:
                guess_frequency[guess] += 1
            else:
                guess_frequency[guess] = 1
            if guess == secret_num:
                print("Correct you won this time")
                wins += 1
            elif guess < secret_num :
                print("Too low!!")   
            else:
                print("Too high!!")  
                
            attempts -= 1
            print("Attempts left:", attempts)
        if not win :
            print("Chaii you lost the correct ans was:", secret_num)  
            loss += 1
    
    elif user == "2":
        print("=========GAME STATS=========")
        print(f"\nTotal Games played: {total_guess}")
        print(f"Wins: {wins}")
        print(f"Losses: {loss}")
        if all_guess:
            running_mean = sum(all_guess) / len(all_guess)
            most_guessed = max(guess_frequency, key=guess_frequency.get)
            least_guessed = min(guess_frequency, key=guess_frequency.get)
            print(f"Total guesses made: {len(all_guess)}")
            print(f"Most guessed num: {most_guessed}")
            print(f"Least guessed num: {least_guessed}")
            print(f"All Guess: {all_guess}")
        else:
            print("No guesses made yet!!!")    
    elif user == "3":
        print("Thanks for playing!!")
        print("Existing game.......")
        break
    else:
        print("Invalid request!!!...")   
        print("Try again......")
