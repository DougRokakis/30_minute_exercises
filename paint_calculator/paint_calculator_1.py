import math
#A can of paint will cover 350 square ft of area 
while True:
    try:
        square_ft_to_paint = int(input("How many square feet do you need to paint? "))
    except ValueError:
        print("Please ensure you type a numerical value")
        continue
    else:
        break
paint_needed = (int(square_ft_to_paint))/350
amount_of_cans_needed = math.ceil(paint_needed)
print("You will need " + str(amount_of_cans_needed) + " gallons of paint to cover " + str(square_ft_to_paint) + " square feet.")