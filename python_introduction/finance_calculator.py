# Prompt the user for their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings (with interest)
interest_rate = 0.05
annual_savings = monthly_savings * 12  # Total savings without interest
projected_savings = annual_savings + (annual_savings * interest_rate)  # Savings with interest

# Output the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
