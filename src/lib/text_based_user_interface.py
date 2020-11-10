from os import system, name
import sys

CURSOR_UP_ONE = "\x1b[1A"
ERASE_LINE = "\x1b[2K"

def framedText(text):
    length = len(text)+2
    print("   ╔", end="")
    for x in range(0, length):
        if x < length-1:
            print("═", end="")
        else:
            print("═╗")
    print("   ║ " + text + " ║")
    print("   ╚", end="")
    for x in range(0, length):
        if x < length-1:
            print("═", end="")
        else:
            print("═╝")

def printText(text, framed):
    if framed:
        framedText(text)
    else:
        print(text)

def textWithIndent(text, indent):
    for x in range(0, indent):
        print(" ", end="")
    print(text)

def inputWithIndent(text, indent):
    for x in range(0, indent):
        print(" ", end="")
    return input(text + " ")

def log(type, content):
    textWithIndent("[" + type + "]: " + content, 3)

def newLine():
    print("")

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def pressAnyKey():
    inputWithIndent("Press any key to continue...", 3)

def deleteLastLines(numOfLines):
    for _ in range(0, numOfLines):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
