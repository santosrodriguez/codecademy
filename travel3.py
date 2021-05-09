current_budget = 3500.75
shirt_expense = 9

# Function to print your budget
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Function to deduct expenses from your budget
def deduct_expense(budget, expense):
  return budget - expense


new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)
