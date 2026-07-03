import random;

print("Welcome to Hangman!");

wordlist = [];

with open("words.txt") as words:
    for line in words:
        if "'" not in line and "-" not in line:
            wordlist.append(line.upper().strip());

secret_word = random.choice(wordlist)

print(type(wordlist));
print(wordlist);
print(secret_word)
