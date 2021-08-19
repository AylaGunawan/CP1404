"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

number_of_sales = float(input("Enter sales: $"))
while number_of_sales >= 0:
    if number_of_sales < 1000:
        bonus = number_of_sales * 0.1
    else:
        bonus = number_of_sales * 0.15
    print(f"Bonus: ${bonus:.2f}")
    number_of_sales = float(input("Enter sales: $"))
print("Farewell")
