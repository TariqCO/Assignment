
theWord = "cat"
hintCount = 2
guessCount = 5

while guessCount >= 1:
    word = input("Guess the word: ")
    
    if word == theWord:
        print(f"You Guessed the right word. It's a {theWord}")
        break
    else:
        guessCount -= 1
        print(f"{guessCount} guess left")
        hint = input("Do you want a hint? (yes/no) ").lower()
        if hint == "yes" and hintCount == 2:
            print(f"It's an animal")
            hintCount -= 1
            print(f"\n{hintCount} hint left")
            continue
        elif hint == "yes" and hintCount == 1:
            print(f"It's a cute.")
            hintCount -= 1
            print(f"\n{hintCount} hints left")
            continue
        else:
            continue
     

