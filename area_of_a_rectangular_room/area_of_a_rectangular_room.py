while True:
    try:
        length_of_room = int(input("What is the length of the room in feet? "))
    except ValueError:
        print("Please ensure that you are typing in an integer.")
    else:
        break
while True:
    try:
        width_of_room = int(input("What is the width of the room in feet? "))
    except ValueError:
        print("Please ensure that you are typing in an integer.")
    else:
        break
total_square_feet=length_of_room*width_of_room
feet_to_meters= total_square_feet/3.2808

print("The area is " + str(total_square_feet) + " square feet or " + str(round(feet_to_meters, 3)) + " square meters.")