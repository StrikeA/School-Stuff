import random

def while1():
    ages = True
    while ages == True:
        user_input = int(input("How old are you? "))
        if user_input < 0:
            print("Please input a valid number")
        else:
            print(f"You are {user_input} years old.")
            break

def While2():
    guess = False
    number = random.randrange(1, 100001)
    while guess == False:
        user_input = int(input("pick a random number "))
        if user_input > number:
            print("to high")
        elif user_input < number:
            print("to low")
        else:
            print("Correct")
            break

