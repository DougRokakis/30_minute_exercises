import math
#A can of paint will cover 350 square ft of area 
print ("You have an L-shaped room? Well ain't that a pickle. We'll need four measurements. I hope you've come prepared!")
while True:
    try: 
        width_rectangle_1 = int(input("What is the width of the first square/rectangle that makes up the L shape? "))
    except ValueError:
        print("Please ensure you type a numerical value.")
        continue
    else:
        break
while True:
    try: 
        length_rectangle_1 = int(input("What is the length of that same first square/rectangle that makes up the L shape? "))
    except ValueError:
        print("Please ensure you type a numerical value.")
        continue
    else:
        break
while True:
    try: 
        width_rectangle_2 = int(input("What is the width of the second square/rectangle that makes up the L shape? "))
    except ValueError:
        print("Please ensure you type a numerical value.")
        continue
    else:
        break
while True:
    try: 
        length_rectangle_2 = int(input("What is the length of that same second square/rectangle that makes up the L shape? "))
    except ValueError:
        print("Please ensure you type a numerical value.")
        continue
    else:
        break
sqft_rectangle_1 = width_rectangle_1*length_rectangle_1
sqft_rectangle_2 = width_rectangle_2*length_rectangle_2
total_sqft_to_paint = sqft_rectangle_1+sqft_rectangle_2
paint_needed = int(total_sqft_to_paint)/350
amount_of_cans_needed = math.ceil(paint_needed)
print("Based on the diameter of the ceiling given you will need " + str(amount_of_cans_needed) + " gallons of paint to cover " + str(total_sqft_to_paint) + " square feet.")