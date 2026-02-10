batch = int(input("Enter Batch year: "))
std= int(input(f"Enter how many student are enrolled in this {batch}?: "))

enrollUni= input("Enter unique code: ")


for i in range(1, std + 1):
    if i > std/2:
        print(f"Unique Enrollemnt Id's: \n{i}-{batch}-{enrollUni}#{i + 2}{i - 1}")
    else:
        print(f"Unique Enrollemnt Id's: \n{i}-{batch}-{enrollUni}@{i + 2}{i - 1}")