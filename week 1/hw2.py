
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %")

    num1 = float(input("Enter first number: "))
    operation = input("Enter operation: ")
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Error! Division by zero."
    elif operation == "%":
        result = num1 % num2
    else:
        result = "Invalid operation"

    print("Result:", result)

calculator()