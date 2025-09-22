# Daily_Reminder 

# Prompt the user for task 

task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority entered. Please enter 'high', 'medium', or 'low'."

# Modify the reminder based on whether the task is time-bound
if time_bound == "yes":
    print(f"Reminder: {reminder} that requires immediate attention today!")
else:
    print(f"Note: {reminder}. Consider completing it when you have free time.")
