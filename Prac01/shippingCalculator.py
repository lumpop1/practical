items = int(input("Enter the number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Enter the number of items: "))
cost = float(input("Enter the shipping cost for each different item: $"))
totalCost = items * cost
if totalCost > 100:
    totalCost *= 0.9
print(totalCost)