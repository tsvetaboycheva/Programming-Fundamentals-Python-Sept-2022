budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25
one_bread_price = eggs_price + flour_price + milk_price / 4
colored_eggs = 0
loaf_of_bread = 0
while budget >= one_bread_price:
    budget -= one_bread_price
    colored_eggs += 3
    loaf_of_bread += 1
    if loaf_of_bread % 3 == 0:
        colored_eggs -= loaf_of_bread - 2
money_left = budget
print(
    f"You made {loaf_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
