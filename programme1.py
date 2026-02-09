

while True:
    steps = int(input("What do you want to print? \n1. Whole Numbers \n2. Even Numbers \n3. Odd Numbers \n\n --> | "))
        
    if steps == 1:
        stopRange = int(input("Enter the Number where you wanna stop: "))
        for i in range(1, stopRange + 1):
            print(i, end=" ")
            
        reset = int(input("\n\nDo you want to  start again? \n1. Yes \n2. No \n\n --> |  "))
        if reset == 1:
            continue
        else:
            print("Exit.. Thank You.")
            break
    elif steps == 2:
        stopRange = int(input("Enter the Number where you wanna stop: "))
        for i in range(0, stopRange + 1, 2 ):
            print(i, end=" ")
        reset = int(input("\n\nDo you want to start again? \n1. Yes \n2. No \n\n --> | "))
        if reset == 1:
            continue
        else:
            print("Exit.. Thank You.")
            break 
    elif steps == 3:
        stopRange = int(input("Enter the Number where you wanna stop: "))
        
        for i in range(1, stopRange + 1, 2):
            print(i, end=" ")
        reset = int(input("\n\nDo you want to start again? \n1. Yes \n2. No \n\n --> | "))
        if reset == 1:
            continue
        else:
            print("Exit.. Thank You.")
            break         
    else:
        print("\nInvalid input, Select within limit.\nRestarting...\n")
        continue