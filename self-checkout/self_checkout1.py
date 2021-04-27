while True:
    try:
        price_item_1 = int(input("Enter the price of item 1: "))
    except ValueError:
        print("Please type a number")
        continue
    else:
        break
while True:
    try:
        quantity_item_1 = int(input("Enter the quantity of item 1: "))
    except ValueError:
        print("Please type a number")
        continue
    else:
        break
while True:
    try:
        price_item_2 = int(input("Enter the price of item 2: "))
    except ValueError:
        print("Please type a number")
        continue
    else:
        break
while True:
    try:
        quantity_item_2 = int(input("Enter the quantity of item 2: "))
    except ValueError:
        print("Please type a number")
        continue
    else:
        break
while True:
    try:
        price_item_3 = int(input("Enter the price of item 3: "))
    except ValueError:
        print("Please type a number")
        continue
    else:
        break
while True:
    try:
        quantity_item_3 = int(input("Enter the quantity of item 3: "))
    except ValueError:
        print("Please type a number")
        continue
    else:
        break
subtotal = (price_item_1*quantity_item_1) + (price_item_2*quantity_item_2) + (price_item_3*quantity_item_3)
tax = subtotal*.055
total = subtotal + tax
print("Subtotal: " + str(subtotal))
print("Tax: " + str(tax))
print("Total: " + str(total))