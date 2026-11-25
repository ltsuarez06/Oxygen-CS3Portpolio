name = input("What is your name? ")
print("Hello, " + name + "! Welcome to the program.")

Number = input("Please enter a number: ")

if int(Number) > 0:
    print("You entered a positive number.")
else:
    print("You entered a negative number.")

    if int(Number) == 0:
        print("You entered zero.")

        Numberequals = input("Please enter another number: ")

        if int(Numberequals) > int(Number):
            if int(Numberequals) > int(Number):
                print("The second number is greater than the first number.")
        else:
                    print("The second number is not greater than the first number.")

if int(Numberequals) == int(Number):
    print("The first number is equal to the second number.")

    score = input("Please enter your score: ")

if int(score) >= 75:
    print("Congratulations! You passed the test.")
else:
    print("Sorry, you did not pass the test. Better luck next time!")

    numberoddeven = input("Please enter a number to check if it is odd or even: ")

    if int(numberoddeven) % 2 == 0:
        print("The number is even.")    
    else:
        print("The number is odd.")