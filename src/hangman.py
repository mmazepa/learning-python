import random

from lib.text_based_user_interface import framedText, textWithIndent, inputWithIndent, log, newLine, clear

def header():
    textWithIndent(" _   _                                         ", 3)
    textWithIndent("| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  ", 3)
    textWithIndent("| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ", 3)
    textWithIndent("|  _  | (_| | | | | (_| | | | | | | (_| | | | |", 3)
    textWithIndent("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|", 3)
    textWithIndent("                   |___/                       ", 3)

def convertToUnderscores(word, board):
    underscores = ""
    for i in range(0, len(word)):
        if board[i] == 0:
            underscores += "_"
        else:
            underscores += word[i]
    return underscores

def printWithSpaces(word, indent):
    for i in range(0, indent):
        print(" ", end="")
    for char in word:
        print(char, end="")
        print(" ", end="")
    print("")

def changeBoard(guess, word, board):
    for i in range(0, len(word)):
        if word[i].lower() == guess.lower():
            board[i] = 1

def isTheEnd(board):
    for i in range(0, len(board)):
        if board[i] == 0:
            return False
    return True

def appendGuessedLetter(guess, guessed):
    if not guess.upper() in guessed:
        guessed.append(guess.upper())
        return True
    return False

hangmanDatabase = [
    "Spider",
    "Crocodile",
    "Programming"
]

number = random.randint(0, len(hangmanDatabase)-1)
word = hangmanDatabase[number]
board = []

for i in range(0, len(word)):
    board.insert(i, 0)

guessed = []
tries = 10
infotext = ""

while (True):
    clear()
    header()
    newLine()

    framedText("Guess the letter in a word, phrase or sentence.")
    newLine()

    if len(infotext) > 0:
        log("INFO", infotext)
        infotext = ""
        newLine()
    else:
        for i in range(0, 2):
            newLine()

    printWithSpaces(convertToUnderscores(word, board), 3)
    printWithSpaces(board, 3);
    newLine()
    textWithIndent("Tries left: " + str(tries), 3)
    textWithIndent("Guessed letters:", 3)
    if len(guessed) > 0:
        printWithSpaces(guessed, 6)
    else:
        textWithIndent("-", 6)
    newLine()

    if isTheEnd(board) or tries == 0:
        break

    guess = inputWithIndent("Guess the letter:", 3)
    if not guess.lower().isalpha():
        infotext = "Please type characters only."
    elif len(guess) > 1:
        infotext = "Please do not cheat. You can guess only one letter at a time."
    elif guess.lower() in word.lower():
        changeBoard(guess, word, board)
        if not appendGuessedLetter(guess, guessed):
            infotext = "This letter has already been guessed."
    else:
        if appendGuessedLetter(guess, guessed):
            tries -= 1
        else:
            infotext = "This letter has already been guessed."
    newLine()
