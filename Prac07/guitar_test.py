class Guitars:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}): ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self, current_year):
        age = current_year - int(self.year)
        if age >= 50:
            vintage = True
        else:
            vintage = False
        return vintage

print("My Guitars!")
guitar_list = []
guitar_name = input("Name: ")
while guitar_name != "":
    guitar_year = str(input("Year: "))
    guitar_cost = float(input("Cost: "))

    guitar_data = [guitar_name, guitar_year, guitar_cost]
    guitar_list.append(guitar_data)
    print("{} has been added.".format(Guitars(guitar_name, guitar_year, guitar_cost)))

    guitar_name = input("Name: ")

count = 0
print("These are my guitars:")
for i in guitar_list:
    string = Guitars(i[0], i[1], i[2])
    count += 1
    age = string.get_age(2014)
    if age == True:
        print("Guitar {}: {} (vintage)".format(count,string))
    else:
        print("Guitar {}: {}".format(count, string))