# Console-based Wordle game

import random
from colorama import Back, Style


WHITE = f"{Back.WHITE} {Style.RESET_ALL}"
YELLOW = f"{Back.YELLOW} {Style.RESET_ALL}"
GREEN = f"{Back.GREEN} {Style.RESET_ALL}"

with open("wordlist.txt", encoding="utf-8") as f:
    words = f.read().split()

word = random.choice(words)

print("Willkommen bei Wordle. Errate das gesuchte Wort.")

guess_number = 0

done = False
while not done:
    if guess_number > 5:
        done = True
    else:
        guess = input("> ").strip().upper()

        if len(guess) != 5:
            print("Das Wort muss fünf Buchstaben lang sein.")
        elif guess not in words:
            print(f"'{guess}' ist kein korrektes deutsches Wort.")
        else:
            guess_number += 1
            print("  ", end="")

            characters = list(word)
            results = [WHITE, WHITE, WHITE, WHITE, WHITE]   # Default: Alles falsch! (weiss)

            for i in range(5):          # Korrekt gesetzte Buchstaben (grün)
                letter = guess[i]
                if letter == word[i]:
                    results[i] = GREEN
                    characters.remove(letter)

            for i in range(5):          # Existierende aber falsch platzierte Buchstaben (gelb)
                letter = guess[i]
                if results[i] != GREEN and letter in characters:
                    results[i] = YELLOW
                    characters.remove(letter)

            print("".join(results))

            if guess == word:
                print(f"Du hast das Wort gefunden!")
                done = True
