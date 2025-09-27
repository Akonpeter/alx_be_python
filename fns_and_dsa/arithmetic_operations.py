# # Arithmetic Operations Function

# from arithmetic_operations import perform_operation

# def main():
#     print("Arithmetic Operations")
#     num1 = float(input("Enter the first number: " ))
#     num2 = float(input("Enter the second number:  "))
#     operation = input("Enter the operation (add, subtract, multiply, divide):").string() .lower()
#     result = perform_operation(num1, num2, operation)
#     print(f"result: {result}")

#     if __name__ == "__main__":
#         main()



# Arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    
    """
    Performs basic arithmetic operations.
    
    Parameters:
        num1 = float (input("Enter the first number: "))

        num2 = float (input("Enter the second number: "))
        
        operation = str (operation("Enter the operation(add, subtract, multiply, divide);").string() .lower()
    
    Returns:
        float or str: The result of the operation, or an error message for invalid cases"""
    
    match operation.lower():
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        case _:
            return "Error: Invalid operation"
        



