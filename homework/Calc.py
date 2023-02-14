def main():
    calc = True
    while calc:
        number1 = float(input("What is your first number? "))
        number2 = float(input("What is your second number? "))
        opp = input("What operation would you like to use addition (+), subtraction (-), multiplication (*), or division (/)? ")
        if opp == "+":
            answer = number1 + number2
        elif opp == "-":
            answer = number1 - number2
        elif opp == "*":
            answer = number1 * number2
        elif opp == "/":
            answer = number1 / number2
        else:
            print("You selected an unsupported operation.")
            break
        print("The answer is:", answer)
        calc_again = input("Would you like to calculate another number (y or n)? ")
        if calc_again != "y":
            print("Thank you for using this calculator.")
            break


main()
