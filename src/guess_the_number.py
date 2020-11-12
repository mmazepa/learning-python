import random

from lib.text_based_user_interface import framedText, textWithIndent, inputWithIndent, log, newLine, clear
from lib.number_validation import typeCorrectNumberLoop

def header():
    textWithIndent(" _____                 _____ _       _____           _           ", 3)
    textWithIndent("|   __|_ _ ___ ___ ___|_   _| |_ ___|   | |_ _ _____| |_ ___ ___ ", 3)
    textWithIndent("|  |  | | | -_|_ -|_ -| | | |   | -_| | | | | |     | . | -_|  _|", 3)
    textWithIndent("|_____|___|___|___|___| |_| |_|_|___|_|___|___|_|_|_|___|___|_|  ", 3)

clear()
header()
newLine()

number = random.randint(0, 100)
framedText("Guess the number from 0 to 100. You'll get a hint if you miss.")
newLine()

count = 1;

while (True):
    x = typeCorrectNumberLoop(count, "Guess the number, attempt no.")
    if not x >= 0 or not x <= 100:
        log("INFO", "The number is not from range [0-100].")
        continue
    elif x == number:
        log(str(count), "Yes, you are correct! The number is " + str(x) + ".")
        newLine()
        break
    elif x < number:
        log(str(count), "Number is greater than " + str(x) + ".")
    elif x > number:
        log(str(count), "Number is lower than " + str(x) + ".")
    newLine()
    count += 1
