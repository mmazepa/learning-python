from lib.text_based_user_interface import inputWithIndent, log

def isNumber(number):
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            log("INFO", "Please type a number.")

def typeCorrectNumberLoop(index, label = "Enter number"):
    number = ""
    while (not isinstance(number, int)) and (not isinstance(number, float)):
        number = inputWithIndent(label + " " + str(index) + ":", 3)
        number = isNumber(number)
    return number;
