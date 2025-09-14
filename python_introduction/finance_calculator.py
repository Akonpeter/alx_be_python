# Finance_calculator.py

# Prompt the user for financial details

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings

monthly_savings = monthly_income - monthly_expenses

# Annual savings without interest
annual_savings = monthly_savings * 12

# Projected savings with 5% interest
interest_rate = 0.05
project_savings = annual_savings + (annual_savings * interest_rate)

# Display result
print("\n--- savings report ---")
print("Your monthly savings are: $", monthly_savings)
print("Your projected savings after one year (with 5% interest) are: $", {project_savings})

