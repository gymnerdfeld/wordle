# Console-based Wordle game

import random
from colorama import Back, Style


W = f"{Back.WHITE} {Style.RESET_ALL}"
Y = f"{Back.YELLOW} {Style.RESET_ALL}"
G = f"{Back.GREEN} {Style.RESET_ALL}"

with open("wordlist.txt", encoding="utf-8") as f:
    words = f.read().split()

word = random.choice(words)

print("Willkommen bei Wordle. Errate das gesuchte Wort.")

done = False
while not done:    
    guess = input("> ").strip().upper()
    if len(guess) != 5:
        print("Das Wort muss fünf Buchstaben lang sein.")
    elif guess not in words:
        print(f"'{guess}' ist kein korrektes deutsches Wort.")
    else:
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
            print(f"Du hast das Wort gefunden!")
            done = True
