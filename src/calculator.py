def isNumber(number):
    try:
        return int(number)
    except ValueError:
        try:
            return float(number)
        except ValueError:
            print("Please type a number.")
            exit();

num1 = input("Enter num1: ")
num1 = isNumber(num1)
num2 = input("Enter num2: ")
num2 = isNumber(num2)

print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
