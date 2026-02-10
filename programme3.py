
stTariq=567
stRafay=623
stJohn=400

print("\n=============== Find your Roll number ===============\n")

name = input("Enter your name: ").lower()
clss = input("Enter your class: ")
sec =  input("Enter your Section: ")



while True:
    print("\nSearch --> \n")
    
    if (name == "tariq rasheed") and (clss == "8") and (sec == "b"):
        for i in range(300 , 800 + 1):
            if stTariq == i:
                print(f"Name: {name}, Roll No.: {i}")
                break
            else:
                print(f"searching list.... {i}")
                continue
            
        break
    elif (name == "rafay shaikh") and (clss == "10") and (sec == "c"):
        for i in range(300 , 800 + 1):
            if stRafay == i:
                print(f"Name: {name}, Roll No.: {i}")
                break
            else:
                print(f"searching list.... {i}")
                continue
            
        break
    elif (name == "john doe") and (clss == "5") and (sec == "a"):
        for i in range(300 , 800 + 1):
            if stJohn == i:
                print(f"Name: {name}, Roll No.: {i}")
                break
            else:
                print(f"searching list.... {i}")
                continue
            
        break
    else:
        print(f"There is no student with these details.")
        break
    