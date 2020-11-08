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

arithmetic_operators = ["+", "-", "*", "/"]

def mainMenu():
    sign = ""
    while (not sign in arithmetic_operators):
        sign = input("Enter arithmetic operator \"+\", \"-\", \"*\" or \"/\": ")
        if sign == "+":
            return str(num1) + " + " + str(num2) + " = " + str(add(num1, num2))
            break
        elif sign == "-":
            return str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2))
            break
        elif sign == "*":
            return str(num1) + " * " + str(num2) + " = " + str(multiply(num1, num2))
            break
        elif sign == "/":
            return str(num1) + " / " + str(num2) + " = " + str(divide(num1, num2))
            break
        print("Please type an arithmetic operator.")

num1 = typeCorrectNumberLoop(1)
num2 = typeCorrectNumberLoop(2)

print(mainMenu())
