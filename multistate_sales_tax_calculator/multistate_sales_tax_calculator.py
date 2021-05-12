from multistate_sales_tax_calculator_dicts import alabama, california, delaware, florida, georgia, hawaii, idaho, kansas, louisiana, maine, nebraska, ohio, pennsylvania, rhode_island, south_carolina, tennessee, utah, vermont, washington

print("This program is designed to assess sales tax in different counties/parishes in Alabama, California, Delaware, Florida, Georgia, Hawaii, Idaho, Kansas, Louisiana, Maine, Nebraska, Ohio, Pennsylvania, Rhode Island, South Carolina, Tennessee, Utah, Vermont, and Washington. Please answer the following questions as accurately as you can.")
while True:
    try:
        order_total = float(input("What is the order amount in dollars? "))
    except:
        print ("Please be sure to input an integer.")
    else:
        break
while True:
    state_living_in = input("Please select from the list of states provided: ")
    if state_living_in.lower() == "alabama":
        for i in alabama.keys():
            print(i)
        
    elif state_living_in.lower() == "california":
        for i in california.keys():
            print(i)

    elif state_living_in.lower() == "delaware":
        for i in delaware.keys():
            print(i)

    elif state_living_in.lower() == "florida":
        for i in florida.keys():
            print(i)

    elif state_living_in.lower() == "georgia":
        for i in georgia.keys():
            print(i)

    elif state_living_in.lower() == "hawaii":
        for i in hawaii.keys():
            print(i)

    elif state_living_in.lower() == "idaho":
        for i in idaho.keys():
            print(i)

    elif state_living_in.lower() == "kansas":
        for i in kansas.keys():
            print(i)

    elif state_living_in.lower() == "louisiana":
        for i in louisiana.keys():
            print(i)

    elif state_living_in.lower() == "maine":
        for i in maine.keys():
            print(i)

    elif state_living_in.lower() == "nebraska":
        for i in nebraska.keys():
            print(i)

    elif state_living_in.lower() == "ohio":
        for i in ohio.keys():
            print(i)

    elif state_living_in.lower() == "pennsylvania":
        for i in pennsylvania.keys():
            print(i)

    elif state_living_in.lower() == "rhode island":
        for i in rhode_island.keys():
            print(i)

    elif state_living_in.lower() == "south carolina":
        for i in california.keys():
            print(i)

    elif state_living_in.lower() == "tennessee":
        for i in tennessee.keys():
            print(i)

    elif state_living_in.lower() == "utah":
        for i in utah.keys():
            print(i)

    elif state_living_in.lower() == "vermont":
        for i in vermont.keys():
            print(i)

    elif state_living_in.lower() == "washington":
        for i in washington.keys():
            print(i)

    else:
        print("Please ensure to choose from the states provided above and check for spelling.")
        continue
    break
while True:
    try:
        county_living_in = str(input("Please select a county from " +state_living_in.capitalize()+ ": "))
    except:
        print("Please type in the name of a county listed.")
    else:
        sales_tax_in_county = str(state_living_in).get(county_living_in.capitalize())
        print("The tax on $" +str(order_total)+  " in " +str(county_living_in)+ " county is " +str(sales_tax_in_county*100)+ "%.\nYour total comes to $" +str(round(order_total + (order_total*sales_tax_in_county), 2))+ ".")
        break