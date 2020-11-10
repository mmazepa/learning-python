from os import system, name

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
