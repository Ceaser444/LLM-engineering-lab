import random 
import sys
import matplotlib.pyplot as x
from collections import Counter
WORD_FILE = "words.txt"
MAX_ATTEMPTS = 6
def load_words(filename = WORD_FILE):
    try:
        with open(filename) as f:
            return[line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError :
        print("Error!! file not found using default words....")  
        return['console','cybernetics', 'nodejs', 'token']   
def hangman_game(words, attempts = MAX_ATTEMPTS):
    if not words:
        print("No words found") 
        return 
    secret_word = random.choice(words)
    guessed = []  
    display= ['_']* len(secret_word)
    print("Welcome to hangman_game\n")
    print("\n" + "_"*50 + "\n")
    try:
        while attempts and '_' in display:
            print("guessed letter: ",','.join(sorted(guessed)) if  guessed else 'None')
            print("Attempts left: ", attempts)
            try:
                guess = input("guess a letter to play or type quit to exit: ").strip().lower() 
            except EOFError :
                print("End-Of-File. Exiting......") 
                return  
            if guess == "quit":
                print("Thanks for playing")
                print("Exiting.....")
                return 
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input enter a single letter")
                continue 
            if guess in guessed:
                print("you have already guessed this letter!!")  
                continue
            guessed.append(guess)
            if guess in secret_word:
                print(f"Wow!! {guess} is in secret word") 
                for idx, ch in enumerate(secret_word):
                    if ch == guess:
                        display[idx] = guess
            else:
                attempts -= 1
                print("sorry try again!!")
            print('word: ', ''.join(display), '\n')   
        if '_' not in display:
            print('You win!!! the word was: ', secret_word)
        else :
            print('You lose! the word was', secret_word)   
    except KeyboardInterrupt:
        print("\n Game interrupted, Bye!!!")       
def word_histogram(filename = WORD_FILE, top_n = 10):
    try:
        words = load_words(filename)
        if not words :
            print("No words found!!")
            return
        counts = Counter(words)   
        most_common = counts.most_common(top_n)
        if not most_common:
            print("No words to display!!")  
            return
        labels, values = zip(*most_common)
        x.figure(figsize = (12, 6))
        x.bar(labels, values, color = 'skyblue', edgecolor= 'black')
        x.title(f"Top {top_n} Word Frequencies", fontsize = 16, fontweight= 'bold')
        x.xlabel("words", fontsize = 12)
        x.ylabel("frequencies", fontsize = 12)
        x.xticks(rotation = 45)
        x.tight_layout()
        x.show()
    except FileNotFoundError as e:
        print(f"Error file not found {e} word_histogram not created!! ")  
def main():
    print("Loading Words.......")
    words= load_words()
    print(f"{len(words)} words loaded successfully!!")
    hangman_game(words) 
    print("creating word frequency histogram")
    word_histogram(top_n = 10)
if __name__ == "__main__":
    main()
