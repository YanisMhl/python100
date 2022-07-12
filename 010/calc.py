def addNumbers(a, b):
    return a + b
def substractNumbers(a, b):
    return a - b
def multiplyNumbers(a, b):
    return a*b
def divideNumbers(a, b):
    return a/b

result = 0
firstNumber = float(input("What's the first number ?: "))
print("+\n-\n*\n/")
operation = input("Pick an operation: ")
secondNumber = float(input("What's the next number ?: "))

if operation == "+":
    result = addNumbers(firstNumber, secondNumber)
elif operation == "-":
    result = substractNumbers(firstNumber, secondNumber)
elif operation == "*":
    result = multiplyNumbers(firstNumber, secondNumber)
else:
    result = divideNumbers(firstNumber, secondNumber)
    
print(f"{firstNumber} {operation} {secondNumber} = {result}")
print(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation")