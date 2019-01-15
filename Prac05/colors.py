colors = {"AliceBlue": "#f0f8ff", "beige": "#f5f5dc", "coral": "#ff7f50", "firebrick": "#b22222", "black": "#000000", "PaleTurquoise": "#afeeee", "MediumBlue": "#0000cd", "MediumAquamarine": "#66cdaa", "maroon": "#b03060", "linen": "#faf0e6"}

color = input("Enter color: ")
while color != "":
    if color in colors:
        print(color, "is", colors[color])
    else:
        print("Invalid color")
    color = input("Enter color: ")