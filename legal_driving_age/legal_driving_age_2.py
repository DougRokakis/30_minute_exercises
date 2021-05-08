while True:
    try:
        age = int(input("WHAATTTT..... is your age? "))
    except ValueError:
        print("Please type in an integer.")
    else:
        if age < 1:
            print ("Please input integer greater than 0.")
            continue
        else:
            break
if age >= 16:
    print("You are old enough to legally drive.")
else:
    print("You are NOT old enough to legally drive.")