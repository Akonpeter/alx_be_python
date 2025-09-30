  # Arithmetic_operations.py

# def perform_operation(num1, num2, operation):

#     match operation.lower():
#         case "add":
#             return num1 + num2
#         case "subtract":
#             return num1 - num2
#         case "multiply":
#             return num1 * num2
#         case "divide":
#             if num2 == 0:
#                 return "Error: Division by zero"
#             return num1 / num2
#         case _:
#             return "Error: Invalid operation"

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
