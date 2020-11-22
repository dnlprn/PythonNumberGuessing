import random

print("The purpose of this game is guessing the number randomly chosen by the computer (between 1 and 100).\n")

pcnumber = random.randint(1, 100) #the computer generates a random number between 1 and 100

usernumberint = pcnumber + 1

while pcnumber != usernumberint:

    usernumberstr = input("Try to guess: ")

    usernumberint = int(usernumberstr) #converts the number from string to integer

    if usernumberint < pcnumber:
        print("Sorry, the number is too low, try again.\n")

    elif usernumberint > pcnumber:
        print("Sorry, the number is too high, try again.\n")

print("Well done! The number is", pcnumber)