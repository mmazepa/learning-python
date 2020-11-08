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

num1 = typeCorrectNumberLoop(1)
num2 = typeCorrectNumberLoop(2)

print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
