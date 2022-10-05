divisor = int(input())
boundary = int(input())
for current_number in range(divisor, boundary + 1):
    if current_number % divisor == 0 and 0 < current_number <= boundary:
        number_to_print = current_number
print(number_to_print)
