tariff = str(input("Which tariff? 11 or 31:"))
while tariff != "11" and tariff != "31":
    print("Invalid")
    tariff = str(input("Which tariff? 11 or 31:"))
if tariff == "11":
    tariff = 0.244618
else:
    tariff = 0.136928
daily = float(input("Enter daily use in kWh: "))
days = int(input("Enter number of billing days:"))
bill = tariff * daily * days
print("Estimated bill: $", round(bill, 2))