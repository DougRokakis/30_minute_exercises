import math

print("PIZZA TIME!")

while True:
    try:
        attending = int(input("How many people? "))
    except ValueError:
        print("Please make sure to input an integer.")
        continue
    else:
        break
while True:
    try:
        pizzas = int(input("How many pizzas do you have? "))
    except ValueError:
        print("Please make sure to input an integer.")
        continue
    else:
        break
slices_per_pizza = pizzas*8
slices_per_person = math.floor(slices_per_pizza/attending)
if slices_per_person == 1:
    piece_or_pieces = " piece"
else:
    piece_or_pieces = " pieces"
leftover_pieces = slices_per_pizza%attending
if leftover_pieces == 1:
    leftover_piece_or_pieces = " leftover piece"
    is_or_are = "is "
else:
    leftover_piece_or_pieces = " leftover pieces"
    is_or_are = "are "
print (str(attending) + " people with " + str(pizzas) + " pizzas.")
print ("Each person gets " + str(slices_per_person) + str(piece_or_pieces) + " of pizza.")
print ("There " +str(is_or_are) + str(leftover_pieces) + str(leftover_piece_or_pieces) + " of pizza.")
