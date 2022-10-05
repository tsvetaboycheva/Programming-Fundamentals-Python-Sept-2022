string_1 = input()
string_2 = input()
last_printed = string_1
for character in range(len(string_1)):
    left_side = string_2[:character + 1]
    right_side = string_1[character + 1:]
    new_string = left_side + right_side
    if new_string != last_printed:
        print(new_string)
        last_printed = new_string
