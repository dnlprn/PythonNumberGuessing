import random

print("The purpose of this game is guessing the number randomly chosen by the computer (between 1 and 100).\n")

pc_number = random.randint(1, 100) #the computer generates a random number between 1 and 100

user_number_integer = pc_number + 1

user_attempts = 1 #used to calculate how many user's attempts to guess the number

while pc_number != user_number_integer:

    user_number_string = input("Try to guess: ")

    user_number_integer = int(user_number_string) #converts the number from string to integer

    if user_number_integer < pc_number:
        print("Sorry, the number is too low, try again.\n")
        user_attempts += 1 

    elif user_number_integer > pc_number:
        print("Sorry, the number is too high, try again.\n")
        user_attempts += 1 

print("Well done! The number is", pc_number,". You took", user_attempts,"attempts to guess.")