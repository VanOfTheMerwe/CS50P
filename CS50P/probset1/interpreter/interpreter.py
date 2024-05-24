math = input("Expression: ")

math = math.split()

x = float(math[0])
y = str(math[1])
z = float(math[2])

if y == "+":
    mathPlus = x + z
    print(mathPlus)
elif y == "-":
    mathMinus = x - z
    print(mathMinus)
elif y == "*":
    mathMultiply = x * z
    print(mathMultiply)
elif y == "/":
    mathDivide = x / z
    print(mathDivide)
else:
    print("Invalid Syntax")

#! Names of values edited for best practice
#! Compare middle to get the correct value from the array
