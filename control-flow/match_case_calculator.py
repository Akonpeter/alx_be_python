# # Calculator

# # Prompt the user for operation 

# num1 = float (input("Enter the first number:") )
# num2 = float (input("Enter the second number:") )

# operation = input("Choose an operation ( +, -, *, /,: )")

# # Match Case for operations

# match operation:

#     # Addition

#     case "+.":
#         result = num1 + num2
#         print(f"The result  is: {result}")

# # Subtraction

#     case "-":
#         result = num1 - num2
#         print(f"The result  is: {result}")

# # Multiplication

#     case  "*": 
#         result = num1 * num2
#         print(f"The result  is: {result}")

# # Divide 
#     case "/":
#          result = num1 / num2
#          print("The result  is: (result).")

# calculator.py

# Prompt the user for numbers and operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Match Case for operations

match operation:
    case "+":
        result = num1 + num2
        print(f"The result is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result  is: {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}")
        else:
            print("Cannot Divide by zero.")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")

    

        