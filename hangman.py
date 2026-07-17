# By Platon Kralin, Sanjay Vellore, Ishanvi Deodhar, Emily Cheng, Sara Juneja.
# Git repo at: https://github.com/Platon-Kralin/crt-project/

import random
import json
import random
#import urllib.request


print("Welcome to Hangman!")

wordlist = []

FALLBACK_WORDS = ["python", "hangman", "computer", "keyboard", "developer", "adobe", "programming"]
MAX_WRONG = 6

 
def get_random_word():
    wordlist = []
    with open("words.txt") as words:
        for line in words:
            if "'" not in line and "-" not in line:
                wordlist.append(line.lower().strip())
   
    return random.choice(wordlist)
# Former Online Code:
#     try:
#         with urllib.request.urlopen("https://random-word-api.herokuapp.com/word",\
#            timeout=5) as response:
#             data = json.load(response)
#             return data[0].lower()
#     except Exception:
#         return random.choice(FALLBACK_WORDS)


def play():
    word = get_random_word().lower()
    guessed = set()
    wrong = 0

    while wrong < MAX_WRONG:
        display = " ".join(c if c in guessed else "_" for c in word)
        print(f"\nWord: {display}")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        if "_" not in display:
            print("\nYou win! The word was:", word)
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess not in word:
            wrong += 1
            print(f"'{guess}' is not in the word.")
        else:
            print(f"Good guess! '{guess}' is in the word.")

    print(f"\nYou lose! The word was: {word}")


if __name__ == "__main__":
    print("=== HANGMAN ===")
    play()

    while input("\nPlay again? (y/n): ").lower().startswith("y"):
        play()
