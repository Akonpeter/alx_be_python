# temp_conversion_tool.py

# Global conversion factors
#    
# FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# # Function to convert Fahrenheit → Celsius
# def convert_to_celsius(fahrenheit: float) -> float:
#     return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# # Function to convert Celsius → Fahrenheit
# def convert_to_fahrenheit(celsius: float) -> float:
#     return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# # Main program logic
# try:
#     # Prompt user for temperature
#     temp_input = input("Enter the temperature value: ")
    
#     # Validate numeric input
#     if not temp_input.replace('.', '', 1).isdigit() and not (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()):
#         raise ValueError("Invalid temperature. Please enter a numeric value.")
    
#     temperature = float(temp_input)
#     unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

#     # Decide which conversion function to call
#     if unit == "C":
#         converted = convert_to_fahrenheit(temperature)
#         print(f"{temperature}°C is {converted:.2f}°F")
#     elif unit == "F":
#         converted = convert_to_celsius(temperature)
#         print(f"{temperature}°F is {converted:.2f}°C")
#     else:
#         print("Invalid temperature. Please enter a numeric value.")

# except ValueError as e:
#     print(e)

# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        
        # Validate numeric value
        if not temp_input.replace('.', '', 1).lstrip('-').isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temp_value = float(temp_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

        if unit == "c":
            result = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is equal to {result:.2f}°F")
        elif unit == "f":
            result = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is equal to {result:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
