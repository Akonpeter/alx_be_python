# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return current_date


# Part 2: Calculate a Future Date
def calculate_future_date(days: int):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)  # add days
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future Date:", formatted_future)
    return future_date


# Main program
if __name__ == "__main__":
    # Show current date and time
    display_current_datetime()

    try:
        # Ask user how many days to add
        days_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_input)
    except ValueError:
        print("Invalid input! Please enter an integer for the number of days.")
