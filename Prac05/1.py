dictionary = {}
names = ["Jack", "Jill", "Harry"]
dobs =  [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
x = 0
for name in names:
    string = str(dobs[x])
    split_string = string.split(",")
    clean_string = split_string[0] + "/" + split_string[1] + "/" + split_string[2]
    dictionary[name] = clean_string[1:-1]
    x += 1

user_input = str(input("Enter something: "))

while user_input not in names:
    print("Error")
    user_input = str(input("Enter something: "))

print(dictionary[user_input])