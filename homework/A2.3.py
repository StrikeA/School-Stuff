# First, you get a plate and set it down on a counter. Then grab a knife and set it next to the plate. Then get a paper towel. Then get your peanut butter, jelly, and bread. Then set those next to the plate. Then open both the jelly and the peanut butter. Then open the bread bag and take 2 pieces of bread and place them on the plate. Then close the bag and put it back. Then take a knife and put it in the peanut butter and get a big scoop on the knife. Then take the knife out and spread the peanut butter on one of the two slices. Then wipe the knife on the paper towl. Then put the knife in the jelly and get a big scoop. Then spread it on the other slice of bread. Then put the knife in the sink. Then put the lid on both the peanut butter container and the jelly. Then put those away. Then enjoy your sandwich.
def lesser_of_evens():
    num1_even = False
    num2_even = False
    while num1_even == False:
        num1 = int(input("input even number 1: "))
        if (num1 % 2) == 1:
            print("Your number is not even enter another ")

        else:
            break

    while num2_even == False:
        num2 = int(input("input even number 2: "))
        if (num2 % 2) == 1:
            print("Your number is not even enter another ")
        elif num2 == num1:
            print("Your number cannot be the same")
        else:
            break

    if num1 > num2:
        print(num2)
    else:
        print(num1)

# lesser_of_evens()

def Animal_Cracker():
    word1_is_word = False
    word2_is_word = False
    while word1_is_word == False:
        word1 = str(input("Enter a word ")).lower()
        if word1.isalpha() == False:
            print("Your word does not just have letters")

        else:
            break
    while word2_is_word == False:
        word2 = str(input("Enter a word ")).lower()
        if word2.isalpha() == False:
            print("Your word does not just have letters")

        else:
            break
    if word1[0] == word2[0]:
        return True

# Animal_Cracker()

def make_twenty():
    num1_isnum = False
    num2_isnum = False
    while num1_isnum == False:
        num1 = input("Input a number ")
        if num1.isnumeric() == False:
            print("Your number is not a number")

        else:
            num1 = int(num1)
            break
    while num2_isnum == False:
        num2 = input("Input a number ")
        if num2.isnumeric() == False:
            print("Your number is not a number")

        else:
            num2 = int(num2)
            break
    if (num1 + num2) == 20:
        print("your numbers add up to twenty")
        return True
    else:
        print("your numbers do not add up to twenty")
        return False

make_twenty()