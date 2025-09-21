# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input(" Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task. Consider completing it when you have free time."
    case _:
        reminder = f"Reminder: '{task}' has an UNKNOWN priority level."

# Add time-sensitive note
if  time_bound == "yes":
    reminder += "This task requires immediate attention today!"

# Display the customized reminder
print(reminder)
