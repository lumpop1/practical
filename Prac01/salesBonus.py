"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sale = float(input("Enter sales: $"))
while sale >= 0:
    if sale < 1000 and sale >= 0:
        bonus = sale * 0.1
    elif sale >= 1000:
        bonus = sale * 0.15
    print(bonus)
    sale = float(input("Enter sales: $"))
print("Invalid number")

