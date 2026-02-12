
print("\n======= Guess the secret word game =========\n")

theWord = "cat"

guessCount = 5
hintCount = 3

while guessCount >= 1:
    word = input("\nGuess the word: ")
    
    if word == theWord:
        print(f"Faaaaah, You Got the right word. It's a {theWord}")
        break
    elif (word != theWord) and (hintCount >= 1) and (guessCount > 1):
        guessCount -= 1
        print(f"\nNo, its not a {word} {guessCount} guess left")
        
        hint = input(f"\n{hintCount} Hints, Do you want a hint? (yes/no) --> | ").lower()
        if hint == "yes" and hintCount == 3:
            print(f"\nIt's an animal")
            hintCount -= 1
            print(f"--> {hintCount} hint left")
            continue
        elif hint == "yes" and hintCount == 2:
            print(f"\nPeople love it.")
            hintCount -= 1
            print(f"--> {hintCount} hints left")
            continue
        elif hint == "yes" and hintCount == 1:
            print(f"\nMeow Meow.")
            hintCount -= 1
            print(f"--> {hintCount} hints left")
            continue        
        else:
            continue
    else:
        guessCount -= 1
        print(f"\nNo, its not a {word} {guessCount} guess left")
        if guessCount == 0:
            break
        else:
            continue
