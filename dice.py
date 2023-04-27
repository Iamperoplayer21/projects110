import random

response = "y"

while response == "y":
    no = random.randint(1, 6)
    if no == 1:
        print("---------")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print("---------")
    elif no == 2:
    elif no == 3:
    elif no == 4:
    elif no == 5:
    elif no == 6:
    response = input("Roll again? (y/n): ")

print("Thanks for playing!")
