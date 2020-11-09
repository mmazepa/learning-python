def isNumber(number):
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            print("Please type a number.")

def typeCorrectNumberLoop(index):
    number = ""
    while (not isinstance(number, int)) and (not isinstance(number, float)):
        number = input("Enter number " + str(index) + ": ")
        number = isNumber(number)
    return number;

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def mainMenu():
    sign = ""
    function = ""
    arithmetic_operators = ["+", "-", "*", "/"]
    while (not sign in arithmetic_operators):
        sign = input("Enter arithmetic operator \"+\", \"-\", \"*\" or \"/\": ")
        if sign == "+":
            function = add
        elif sign == "-":
            function = subtract
        elif sign == "*":
            function = multiply
        elif sign == "/":
            function = divide
        else:
            print("Please type an arithmetic operator.")
    print(str(num1) + " " + sign + " " + str(num2) + " = " + str(function(num1, num2)))

num1 = typeCorrectNumberLoop(1)
num2 = typeCorrectNumberLoop(2)

mainMenu()
