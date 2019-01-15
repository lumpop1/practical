numbers = []

for i in range(0,5):
    num = int(input("Number{}:".format(i+1)))
    while num < 0:
        print("Error")
        num = int(input("Number{}:".format(i+1)))
    numbers.append(num)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))