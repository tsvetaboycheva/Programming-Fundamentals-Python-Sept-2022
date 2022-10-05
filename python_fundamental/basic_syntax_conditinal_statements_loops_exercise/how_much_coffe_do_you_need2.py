command = input()
needed_coffees = 0
while command != "END":
    if command.lower() == "coding" or \
            command.lower() == "dog" or \
            command.lower() == "cat" or \
            command.lower() == "movie":
        if command.islower():
            needed_coffees += 1
        else:
            needed_coffees += 2
    command = input()
if needed_coffees <= 5:
    print(needed_coffees)
elif needed_coffees > 5:
    print(f"You need extra sleep")
