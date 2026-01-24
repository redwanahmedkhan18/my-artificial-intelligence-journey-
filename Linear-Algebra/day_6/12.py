# Expense Tracker

# Goal: Multiple return values

# Task:
# Function receives a list of expenses and returns:

# total

# average

# highest expense

# analyze_expenses([100, 50, 200])
# → (350, 116.67, 200)


# 💡 Skill: Returning tuples

def analyze_expenses(expenses):
    total=sum(expenses)
    average=(sum(expenses)/(len(expenses)))
    average=round(average,2)

    highest_expense=max(expenses)

    return (total,average,highest_expense)


print(analyze_expenses([100, 50, 200]))