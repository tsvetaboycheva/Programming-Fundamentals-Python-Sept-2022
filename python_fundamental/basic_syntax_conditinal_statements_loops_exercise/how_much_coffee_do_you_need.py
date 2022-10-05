command = input()
needed_coffees = 0
while command != "END":
    if command == "coding" or \
            command == "dog" or \
            command == "cat" or \
            command == "movie":
        needed_coffees += 1
    elif command == "CODING" or \
            command == "DOG" or \
            command == "CAT" or \
            command == "MOVIE":
        needed_coffees += 2
    command = input()
if needed_coffees <= 5:
    print(needed_coffees)
elif needed_coffees > 5:
    print(f"You need extra sleep")
