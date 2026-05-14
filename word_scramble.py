import random
# ----------------------------------------------------
# PROVIDED HELPER FUNCTIONS (DO NOT MODIFY)
# ----------------------------------------------------
def load_words(filename="words.txt"):
    """
    Loads the word list from a file and returns a list of words.
    Each word is assumed to be in lowercase.
    """
    print("Loading word list from file...")
    with open(filename, 'r') as f:
        wordlist = f.read().split()
    print(f"{len(wordlist)} words loaded")
    return wordlist
def choose_word(wordlist):
    """
    wordlist: list of strings
    returns: string, a randomly chosen word from the list
    """
    return random.choice(wordlist)
def scramble_word(secret_word):
    """
    Scrambles the letters of the given secret word and prints the scrambled version.
    Does not return anything.
    """
    letters = list(secret_word)
    random.shuffle(letters)
    scrambled = ''.join(letters)
    print(f"Scrambled word: {scrambled}")
# ----------------------------------------------------
# FUNCTIONS TO IMPLEMENT
# ----------------------------------------------------
# Task 1.1
def input_check(secret_word):
    while True:
        raw = input("Your guess: ")

        # Build guess_cleaned: only alpha characters, lowercased
        guess_cleaned = ""
        for ch in raw:
            if ch.isalpha():
                guess_cleaned += ch.lower()

        # Validate: sorted letters must match those of the secret word
        if sorted(guess_cleaned) == sorted(secret_word):
            return guess_cleaned
        else:
            print("Invalid input. Please use only the letters from the secret word.")
# Task 1.2
def has_player_won(secret_word, user_guess):
    return secret_word == user_guess
# Task 1.3
def get_word_progress(secret_word, user_guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == user_guess[i]:
            result += secret_word[i]
        else:
            result += "*"
    return result
# Task 2.1, 2.2
def word_scramble():
    word_list = load_words()

    # Task 2.1 - Game setup
    secret_word = choose_word(word_list)
    print("Welcome to Word Scramble!")
    scramble_word(secret_word)
    attempts = 5
    print(f"You have {attempts} attempts to guess the original word.")

    # Task 2.2 - Main interaction loop
    while attempts > 0:
        print()
        user_guess = input_check(secret_word)

        if has_player_won(secret_word, user_guess):
            print(f"Congratulations! You guessed the word: {secret_word}")
            return

        attempts -= 1
        progress = get_word_progress(secret_word, user_guess)
        print(f"Incorrect. Progress: {progress}")
        print(f"Attempts left: {attempts}")

    # Ran out of attempts
    print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
if __name__ == "__main__":
    word_scramble()
