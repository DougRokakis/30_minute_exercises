while True:
    feet_or_meters = str(input("Did you measure the room in feet or meters? "))
    if feet_or_meters == 'feet':
        while True:
            try:
                length_of_room_feet = int(input("What is the length of the room in feet? "))
            except ValueError:
                print("Please ensure that you are typing in an integer.")
            else:
                break
        while True:
            try:
                width_of_room_feet = int(input("What is the width of the room in feet? "))
            except ValueError:
                print("Please ensure that you are typing in an integer.")
            else:
                break
        total_square_feet=length_of_room_feet*width_of_room_feet
        feet_to_meters= total_square_feet/3.2808
        print("The area is " + str(total_square_feet) + " square feet or " + str(round(feet_to_meters, 3)) + " square meters.")
        break
    elif feet_or_meters == 'meters':
        while True:
            try: 
                length_of_room_meters = int(input("What is the length of room in meters? "))
            except ValueError:
                print("Please ensure that you are typing in an integer.")
            else:
                break
        while True:
            try:
                width_of_room_meters = int(input("What is the width of room in meters? "))
            except ValueError:
                print("Please ensure that you type in an integer.")
            else:
                break
        total_square_meters=length_of_room_meters*width_of_room_meters
        meters_to_feet= round(total_square_meters*3.2808, 3)
        print("The area is " + str(total_square_meters)+ " square meters or " + str(meters_to_feet) + " square feet.")
        break
    else:
        print ("Please select from the two options given.")
        continue