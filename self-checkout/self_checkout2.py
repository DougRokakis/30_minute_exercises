price_items = []
quantity_items = []
is_it_over_yet = 0
while is_it_over_yet == 0:
    price_items = str(input("Enter the price of the item: "))
    quantity_items = str(input("Enter the quantity of the items: "))
    is_it_over_yet = input("If you have finished inputting your purchases, press 1. If you have more to add please press 0.")
pre_subtotal = [a*b for a,b in zip(price_items, quantity_items)]
subtotal_lst = []
for i in pre_subtotal:
    subtotal_lst.append(i)
subtotal = sum(subtotal_lst)
tax = subtotal*.055
total = subtotal + tax
print("Subtotal: " + str(subtotal))
print("Tax: " + str(tax))
print("Total: " + str(total))