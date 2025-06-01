number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))
calculator = input("Please choose an operation (+, -, *, /):")

if calculator == "+":
    print(number1 + number2)
elif calculator == "-":
    print(number1 - number2)
elif calculator == "*":
    print(number1 * number2)
elif calculator == "/":
    if number2 == 0:
        print("Division by zeoro is not allowed")
    else:
        print(number1 / number2)
else:
    print("That's not a valid operation. Please try again")
    