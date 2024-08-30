# Console-based Wordle game

import random
from colorama import Back, Style


W = f"{Back.WHITE} {Style.RESET_ALL}"
Y = f"{Back.YELLOW} {Style.RESET_ALL}"
G = f"{Back.GREEN} {Style.RESET_ALL}"

with open("wordlist.txt", encoding="utf-8") as f:
    words = f.read().split()

word = random.choice(words)

print("gib mau es wort i und versuech z richtigä z erratä")

guess_number = 0

done = False
while not done:
    if guess_number > 5:
        done = True
    else:
        guess = input("> ").strip().upper()

        if len(guess) != 5:
            print("Es muäs 5 buächstabä lang si :(")
        elif guess not in words:
            print(f"'{guess}' isch kes dütsches Wort :(")
        else:
            guess_number += 1
            print("  ", end="")

            characters = list(word)
            results = [W, W, W, W, W]   # Default: Alles falsch! (weiss)

            for i in range(5):          # Korrekt gesetzte Buchstaben (grün)
                c = guess[i]
                if c == word[i]:
                    results[i] = G
                    characters.remove(c)

            for i in range(5):          # Existierende aber falsch platzierte Buchstaben (gelb)
                c = guess[i]
                if results[i] != G and c in characters:
                    results[i] = Y
                    characters.remove(c)

            print("".join(results))

            if guess == word:
                print(f"Du hesches gfungä!!")
                done = True
