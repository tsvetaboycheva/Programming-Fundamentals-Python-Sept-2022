numbers_of_orders = int(input())
total_price = 0
for current_order in range(numbers_of_orders):
    price_pre_capsule = float(input())
    days_of_month = int(input())
    capsule_per_day = int(input())
    if price_pre_capsule < 0.01 or price_pre_capsule > 100:
        continue
    elif days_of_month < 1 or days_of_month > 31:
        continue
    elif capsule_per_day < 1 or capsule_per_day > 2000:
        continue
    total = price_pre_capsule * days_of_month * capsule_per_day
    total_price = total_price + total
    print(f"The price for the coffee is: ${total:.2f}")
print(f"Total: ${total_price:.2f}")
