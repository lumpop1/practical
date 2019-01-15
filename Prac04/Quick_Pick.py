import random

quick_pick = int(input("How many quick picks:"))

for i in range(quick_pick):
    print(random.randint(1, 45), random.randint(1, 45),random.randint(1, 45),random.randint(1, 45),random.randint(1, 45))