# Prompt user for the first number
num1 = float(input("Enter the first number: "))
# Prompt user for the second number
num2 = float(input(" Enter the second number: "))
# Ask for the operation to perform
operation = input("Choose the operation (+, -, *, /): ")
# Perform the calculation using match-case statement
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        # Handle division by zero case
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")
