import math
#A can of paint will cover 350 square ft of area 

square_ft_to_paint = input("How many square feet do you need to paint? ")

paint_needed = (int(square_ft_to_paint))/350
amount_of_cans_needed = math.ceil(paint_needed)
print("You will need " + str(amount_of_cans_needed) + " gallons of paint to cover " + square_ft_to_paint + " square feet.")