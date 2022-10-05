name = input()
while name != "Welcome!" and name != "Voldemort":
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
else:
    if name == "Voldemort":
        print(f"You must not speak of that name!")
    elif name == "Welcome!":
        print(f"Welcome to Hogwarts.")
