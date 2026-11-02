import random

def play_hangman():
    # 1. Use a small list of 5 predefined words (no file/API)
    words = ["python", "script", "coding", "laptop", "internet"]
    secret_word = random.choice(words)
    
    # Track game state
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    # Create the hidden word display (e.g., "_ _ _ _ _ _")
    display_word = ["_"] * len(secret_word)
    
    print("===================================")
    print("      Welcome to Hangman!          ")
    print("===================================")
    print(f"The word has {len(secret_word)} letters.")
    print(f"You can make {max_incorrect} incorrect guesses.\n")

    # 2. Main game loop using a while loop
    while incorrect_guesses < max_incorrect and "_" in display_word:
        print("Word: " + " ".join(display_word))
        print(f"Incorrect guesses remaining: {max_incorrect - incorrect_guesses}")
        
        # Basic console input
        guess = input("Guess a letter: ").lower()
        
        # Input validation (ensure it's a single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.\n")
            continue
            
        guessed_letters.append(guess)
        
        # 3. if-else logic for checking the guess
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.\n")
            # Replace underscores with the correct letter
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.\n")
            incorrect_guesses += 1

    # Game Over / Win condition
    if "_" not in display_word:
        print("===================================")
        print(f"Congratulations! You guessed the word: {secret_word.upper()}")
        print("===================================")
    else:
        print("===================================")
        print(f"Game Over! You ran out of guesses.")
        print(f"The word was: {secret_word.upper()}")
        print("===================================")

# This ensures the game runs when you execute the script in VS Code
if __name__ == "__main__":
    play_hangman()