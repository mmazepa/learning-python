from lib.text_based_user_interface import framedText, textWithIndent, inputWithIndent, log, newLine, clear, pressAnyKey
from lib.elementary_arithmetic import add, subtract, multiply, divide

appTurnedOn = True
calculations = []

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
        number = inputWithIndent("Enter number " + str(index) + ":", 3)
        number = isNumber(number)
    return number;

def calculation(num1, num2):
    sign = ""
    function = ""
    arithmetic_operators = ["+", "-", "*", "/"]
    while (not sign in arithmetic_operators):
        sign = inputWithIndent("Enter arithmetic operator \"+\", \"-\", \"*\" or \"/\":", 3)
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
    calculation = str(num1) + " " + sign + " " + str(num2) + " = " + str(function(num1, num2))
    global calculations
    calculations.append(calculation)
    textWithIndent(calculation, 6)

def calculationMenu():
    calculation(typeCorrectNumberLoop(1), typeCorrectNumberLoop(2))
    newLine()
    pressAnyKey()

def viewHistory():
    framedText("HISTORY")
    newLine()
    global calculations
    if len(calculations) == 0:
        textWithIndent("There is no calculations in history.", 3)
    else:
        index = 1
        textWithIndent("History of calculations length: " + str(len(calculations)) ,3)
        newLine()
        for calculation in calculations:
            textWithIndent("[" + str(index) + "] " + calculation, 6)
            index += 1
    newLine()

while (appTurnedOn):
    clear()
    header()
    framedText("Welcome in the calculator with text-based user interface.")
    newLine()
    # global calculations
    log("INFO", "Calculator was used " + str(len(calculations)) + " times.")
    newLine()

    textWithIndent("What do you want to do?", 3)
    textWithIndent("1. Calculation", 6)
    textWithIndent("2. View history", 6)
    textWithIndent("3. Exit", 6)

    while (True):
        action = inputWithIndent("Decision:", 3);
        if (action == "1"):
            newLine()
            calculationMenu()
            break
        elif (action == "2"):
            newLine()
            viewHistory()
            pressAnyKey()
            break
        elif (action == "3"):
            log("INFO", "Okay, goodbye and have a nice day!")
            newLine()
            quit();
        else:
            log("INFO", "Unrecognised option, type \"1\" (calculation) or \"2\" (view history).")
