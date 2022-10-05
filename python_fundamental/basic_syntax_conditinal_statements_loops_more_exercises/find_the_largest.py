number = input()
biggest = 0
output = 0
for index in range(len(number)):
    new = number[::]
    if new == 9:
        biggest = new
        new -= 1
        output += biggest
        print(output)
    else:
        pass
print(output)
