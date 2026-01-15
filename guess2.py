import random 
import statistics 
#global statistics for variables 
games_played = 0
games_won = 0
games_lost = 0
all_guesses = []
winning_guesses = []
guess_frequency = {}
#game play 
def play_game():
    global games_played,games_won,games_lost,all_guesses, winning_guesses,guess_frequency
    #generate num from 1 to 50
    secret_num = random.randint(1, 50)
    attempts= 0
    game_guesses = []
    
    print("="* 49)
    print("NEW GAME STARTED")
    print("I am thinking of a number between 1 to 50")
    print("="* 49)
    # main core
    while True:
        try:
            guess= int(input(f"\nAttempt #{attempts + 1}guess a num between(1-50): "))
            if guess < 1 or guess > 50:
                print("Please enter a number between 1-50")
                continue 
            attempts += 1
            game_guesses.append(guess)
            all_guesses.append(guess)
            
            if guess in guess_frequency:
                guess_frequency[guess] += 1
            else:
                guess_frequency[guess] = 1
            
            if guess < secret_num:
                print(f"{guess} is too low Try again...") 
            elif guess > secret_num:
                print(f"{guess} is too high Try again...")  
            else:
                print("\nCONGRATULATON🎊🎉!! you guessed it")
                print(f"The num was {secret_num}")
                print(f"You found it in {attempts} attempt(s)")
                
                games_won += 1
                winning_guesses.append(secret_num)
                break 
            
            if attempts >= 10:
                print("\nGAME OVER!!! you've used all your attempts")
                print(f"The secret number was: {secret_num}")
                print(f"Your guesses {game_guesses}")
                
                games_lost += 1
                break 
        except ValueError :
            print("Invalid request!!, enter a number between 1-50")    
              
def show_stats():
    print("="* 49)
    print("GAME STATS")
    print("="* 49)
    
    print("====BASIC STATS====")
    print(f" •Games played: {games_played}")
    print(f" •Games won: {games_won}")
    print(f" •Games lost: {games_lost}")
    
    if games_played > 0:
        win_rate = (games_won/games_played)* 100
        print(f" •Win rate: {win_rate:.1f}%")
        
    if len(all_guesses) > 0:
        avg = statistics.mean(all_guesses)
        print(f"RUNNING MEAN(average of all guesses) {avg:.2f}")
    
    if guess_frequency:
        most_guessed = max(guess_frequency, key=guess_frequency.get)   
        times_guessed = guess_frequency[most_guessed]
        
        print("\nMOST FREQUENT GUESSES")
        print(f" •Most guessed num: {most_guessed} (guessed {times_guessed} times)")
        
        
        sorted_guesses = sorted(guess_frequency.items(), key= lambda x:x[1], reverse=True)[:5]
        print("\n •Top 5 most guessed num: ".upper())
        for number, count in sorted_guesses:
            print(f" -{number}: {count} time(s)")
    
    if winning_guesses:
        print("\n WINNING NUMBERS(numbers you correctly guessed)") 
        
        win_freq = {}
        for num in winning_guesses:
            if num in win_freq:
                win_freq[num] += 1
            else:
                win_freq[num] = 1
        unique_wins = list(win_freq.keys())
        print(f"You have won with these numbers: {sorted(unique_wins)}")     
        
        if len(win_freq) > 1:
            most_common_win = max(win_freq, key=win_freq.get)
            print(f" •Most common wining number: {most_common_win}")
    if guess_frequency:
        print("\nGUESS DISTRACTION (1-50)")   
        never_guessed = [num for num in range(1, 51) if num not in guess_frequency]
        print(f"\n •Number never guessed: {len(never_guessed)}")
        if len(never_guessed) <= 10:
            print(f".   {never_guessed}")
        
        print(f"     •Unique numbers guessed: {len(guess_frequency)}")
        
def main():
    global games_played
    
    print("WELCOME TO NUMBER GUESSING GAME")
    print("=================================")
    
    while True:
        print("\n" + "-" * 40)
        print("MAIN MENU")
        print("-" * 40)
        print("•1 play game")
        print("•2 View stats")
        print("•3 Reset stats")
        print("•4 Exit")
        
        choice= input("\nEnter your choice: ")
        
        if choice== "1":
            games_played += 1
            play_game()
            
        elif choice == "2":
            if games_played == 0:
                print("No games played yet!!")
            else:
                show_stats()  
        
        elif choice == '3':
            confirm = input("Are you sure, you want to reset stats: ").lower()   
            if confirm.lower() == "yes":
                global games_won, games_lost,all_guesses, winning_guesses, guess_frequency
                games_played = 0
                games_won = 0
                games_lost = 0
                all_guesses = []
                winning_guesses = []
                guess_frequency = {}
                print("All stats have been reset")
        
        elif choice == "4":
            print("\nThanks for playing") 
            if games_played > 0:
                print("Final stats")  
                print(f" •Games played: {games_played}")  
                print(f" •Games won: {games_won}")
                print(f" •Win rate: {(games_won/games_played*100):.1f}%")
            print("Existing......")
            break
        
        else:
            print("Invalid choice pls try again!!!!")    

if __name__ == "__main__" :
    main()        
