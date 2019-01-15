cents = float(input("Enter cents per kWh:"))
dailyUse = float(input("Enter daily use in kWh:"))
days = int(input("Enter number of billing days:"))
bill = cents * dailyUse * days / 100
print("Estimated bill: $ ", bill)