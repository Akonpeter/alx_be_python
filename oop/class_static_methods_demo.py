class Calculator:
    
    # Class attribute

    calculation_type = "Arithmetic Operations"

    # Static method
    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    # Class method
    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers and print the calculation type."""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b


# Example usage
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
