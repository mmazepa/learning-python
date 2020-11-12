import random

from lib.text_based_user_interface import framedText, textWithIndent, inputWithIndent, log, newLine, clear

def header():
    textWithIndent(" _____                 _____ _       _____           _           ", 3)
    textWithIndent("|   __|_ _ ___ ___ ___|_   _| |_ ___|   | |_ _ _____| |_ ___ ___ ", 3)
    textWithIndent("|  |  | | | -_|_ -|_ -| | | |   | -_| | | | | |     | . | -_|  _|", 3)
    textWithIndent("|_____|___|___|___|___| |_| |_|_|___|_|___|___|_|_|_|___|___|_|  ", 3)

clear()
header()
newLine()

number = random.randint(0, 100)
# textWithIndent("THE NUMBER IS: " + str(number), 3)
# newLine()
framedText("Guess the number from 0 to 100. You'll get a hint if you miss.")
newLine()

times = 0;

while (True):
    x = int(inputWithIndent("Guess the number: ", 3))
    if x == number:
        log("INFO", "Yes, you are correct! The number is " + str(x) + ".")
        newLine()
        break
    elif x < number:
        log("INFO", "Number is greater than " + str(x) + ".")
    elif x > number:
        log("INFO", "Number is lower than " + str(x) + ".")
