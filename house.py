name = input("What's your name? ")
"""
if name == "Harry":
    print("Gryffindor")
elif name == "Hermoine":
    print("Griffindor")
elif name == "Ron":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

"""

"""
if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryffindor")

elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

"""

"""
match name: 
    case "Harry":
        print("Gryffindor")
    case "Hermoine":
            print("Gryffindor")
    case "Ron":
            print("Gryffindor")
    case "Draco":
            print("Slytherin")
    case _:
            print("Gryffindor")
"""

match name: 
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
            print("Slytherin")
    case _:
            print("Who?")