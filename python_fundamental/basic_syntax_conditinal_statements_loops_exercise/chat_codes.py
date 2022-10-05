number_of_messages = int(input())
for message in range(number_of_messages):
    number = int(input())
    if number == 88:
        print(f"Hello")
    elif number == 86:
        print(f"How are you?")
    elif number < 88 and message != 86:
        print(f"GREAT!")
    else:
        print(f"Bye.")
