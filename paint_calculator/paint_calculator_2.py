import math
#A can of paint will cover 350 square ft of area 
print ("Let's calulate the square footage of your round room")
while True:
    try: 
        diameter_of_room = int(input("What is the diameter of the ceiling you wish to paint? "))
    except ValueError:
        print("Please ensure you type a numerical value.")
        continue
    else:
        break
square_ft_to_paint = (math.pi)*(diameter_of_room/2)**2
paint_needed = int(square_ft_to_paint)/350
amount_of_cans_needed = math.ceil(paint_needed)
print("Based on the diameter of the ceiling given you will need " + str(amount_of_cans_needed) + " gallons of paint to cover " + str(square_ft_to_paint) + " square feet.")