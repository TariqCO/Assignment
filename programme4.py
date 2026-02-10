batch = int(input("Enter Batch year: "))
std= int(input(f"Enter how many student are enrolled in this {batch}?: "))

enrollUni= input("Enter unique code: ")

for i in range(1, std + 1):
    for j in range (1, 5 + 1, 2):
        for k in range(4):
            print(f"Unique Enrollemnt Id's: \n {i}-{batch}-{enrollUni}#{j}{k}")