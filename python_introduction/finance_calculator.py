income = int(input("Enter your monthly income : "))
expenses = int(input("Enter your monthly expenses : "))
monthlySavings = income - expenses
projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * 0.05)
print(f"Your monthly savings are ${monthlySavings}")
print(f"Projected savings after one year, with interest, is : ${int(projectedSavings)}")