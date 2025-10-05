# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers, handling non-numeric inputs and division by zero.
    Returns a message indicating the result or the type of error.
    """
    try:
        # Convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Attempt the division
        result = numerator / denominator
        return f"The result of dividing {numerator} by {denominator} is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
