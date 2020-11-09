from lib.text_based_user_interface import framedText, textWithIndent, log, newLine
from lib.elementary_arithmetic import add, subtract, multiply, divide

def header():
    print("     ____      _            _       _             ")
    print("    / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ ")
    print("   | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|")
    print("   | |__| (_| | | (__| |_| | | (_| | || (_) | |   ")
    print("    \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_| \n")

def isNumber(number):
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            log("INFO", "Please type a number.")

def typeCorrectNumberLoop(index):
    number = ""
    while (not isinstance(number, int)) and (not isinstance(number, float)):
        number = input("   Enter number " + str(index) + ": ")
        number = isNumber(number)
    return number;

def mainMenu(num1, num2):
    sign = ""
    function = ""
    arithmetic_operators = ["+", "-", "*", "/"]
    while (not sign in arithmetic_operators):
        sign = input("   Enter arithmetic operator \"+\", \"-\", \"*\" or \"/\": ")
        if sign == "+":
            function = add
        elif sign == "-":
            function = subtract
        elif sign == "*":
            function = multiply
        elif sign == "/":
            function = divide
        else:
            log("INFO", "Please type an arithmetic operator.")
    newLine()
    textWithIndent("Your result is:", 3)
    textWithIndent(str(num1) + " " + sign + " " + str(num2) + " = " + str(function(num1, num2)), 6)

header()
framedText("Welcome in the calculator with text-based user interface.")
newLine()

mainMenu(typeCorrectNumberLoop(1), typeCorrectNumberLoop(2))
newLine()
