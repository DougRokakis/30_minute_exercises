price_item_1 = int(input("Enter the price of item 1: "))
quantity_item_1 = int(input("Enter the quantity of item 1: "))
price_item_2 = int(input("Enter the price of item 2: "))
quantity_item_2 = int(input("Enter the quantity of item 2: "))
price_item_3 = int(input("Enter the price of item 3: "))
quantity_item_3 = int(input("Enter the quantity of item 3: "))
subtotal = (price_item_1*quantity_item_1) + (price_item_2*quantity_item_2) + (price_item_3*quantity_item_3)
tax = subtotal*.055
total = subtotal + tax
print("Subtotal: " + str(subtotal))
print("Tax: " + str(tax))
print("Total: " + str(total))