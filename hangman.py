import random

WORDS = ["python", "hangman", "computer", "keyboard", "developer", "adobe", "programming"]
MAX_WRONG = 6


def play():
    word = random.choice(WORDS)
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
