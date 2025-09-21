# Daily_Reminder 

# Prompt the user for task 

task = input("Enter your task: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority

match priority:

    case "high":
        reminder = (f"Reminder: '{task}' is a high priority task")
   
    case "low":
        reminder = (f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
# Add time-sensitive note

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
     
# Display the customized reminder
print(reminder)
