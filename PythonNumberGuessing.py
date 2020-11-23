import random

print("The purpose of this game is guessing the number randomly chosen by the computer (between 1 and 100).\n")

pcnumber = random.randint(1, 100) #the computer generates a random number between 1 and 100

usernumberint = pcnumber + 1

userattempts = 1 #used to calculate how many user's attempts to guess the number

while pcnumber != usernumberint:

    usernumberstr = input("Try to guess: ")

    usernumberint = int(usernumberstr) #converts the number from string to integer

    if usernumberint < pcnumber:
        print("Sorry, the number is too low, try again.\n")
        userattempts += 1 

    elif usernumberint > pcnumber:
        print("Sorry, the number is too high, try again.\n")
        userattempts += 1 

print("Well done! The number is", pcnumber,". You took", userattempts,"attempts to guess.")