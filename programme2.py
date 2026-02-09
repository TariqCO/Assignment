
x = 32

while True:
    r = int(input("Enter the range number, to find the secret number within the range: "))
    if r >= x:
        for i in range(r + 1):
            if i == x:
                print(f"Secret number found in this range --> secret num: {x}")
                continue
            else:
                print(f"Searching... {i}")        
        break
    else:
        ans = input(f"\nSecret number not found in this range. Do you want to try again? (yes/no): ")
        if ans == "yes":
            continue
        else:
            print("\nThank You.")
            break
