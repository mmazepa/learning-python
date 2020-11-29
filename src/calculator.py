from datetime import datetime
import math

from lib.text_based_user_interface import framedText, textWithIndent, inputWithIndent, log, newLine, clear, pressAnyKey, deleteLastLines
from lib.elementary_arithmetic import add, subtract, multiply, divide
from lib.number_validation import typeCorrectNumberLoop

calculations = []
calculationsPerPage = 10

def header():
    textWithIndent("  ____      _            _       _             ", 3)
    textWithIndent(" / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ ", 3)
    textWithIndent("| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|", 3)
    textWithIndent("| |__| (_| | | (__| |_| | | (_| | || (_) | |   ", 3)
    textWithIndent(" \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   ", 3)

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
            while num2 == 0:
                log("INFO", "Division by zero is not allowed!")
                num2 = typeCorrectNumberLoop(2, "Change number")
        else:
            log("INFO", "Please type an arithmetic operator.")
    newLine()
    textWithIndent("Your result is:", 3)
    calculation = str(num1) + " " + sign + " " + str(num2) + " = " + str(function(num1, num2))
    calculations.insert(0, [getCurrentDatetime(), calculation])
    textWithIndent(calculation, 6)

def calculationMenu():
    calculation(typeCorrectNumberLoop(1), typeCorrectNumberLoop(2))
    newLine()
    pressAnyKey()

def viewHistory():
    framedText("HISTORY")
    newLine()
    if len(calculations) == 0:
        textWithIndent("There is no calculations in history.", 3)
    else:
        textWithIndent("History of calculations length: " + str(len(calculations)), 3)
        newLine()
        pages = int(math.ceil(len(calculations)/calculationsPerPage))
        for page in range(0, pages):
            textWithIndent("Page " + str(page + 1) + "/" + str(pages), 3)
            newLine()
            for index in range(page*calculationsPerPage, (page+1)*calculationsPerPage):
                textWithIndent("[" + calculations[index][0] + "] " + calculations[index][1], 6)
                if len(calculations) == index+1:
                    break
            if page != pages-1:
                newLine()
                pressAnyKey()
                deleteLastLines(14)
    newLine()

def getCurrentDatetime():
    now = datetime.now()
    dt_string = now.strftime("%Y.%m.%d %H:%M:%S")
    return dt_string

while (True):
    clear()
    header()
    newLine()

    framedText("Welcome in the calculator with text-based user interface.")
    newLine()
    log("INFO", "Calculator was used " + str(len(calculations)) + " times.")
    newLine()

    textWithIndent("What do you want to do?", 3)
    textWithIndent("1. Calculation", 6)
    textWithIndent("2. View history", 6)
    textWithIndent("3. Exit", 6)

    while (True):
        action = inputWithIndent("Decision:", 3)
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
            quit()
        else:
            log("INFO", "Unrecognised option, type \"1\" (calculation) or \"2\" (view history).")
