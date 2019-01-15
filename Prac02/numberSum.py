in_file = open("number.txt", "r")
total = 0
for line in in_file:
   number = int(line)
   total += number
print(total)
in_file.close()