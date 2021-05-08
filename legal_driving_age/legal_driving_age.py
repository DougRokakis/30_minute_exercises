while True:
    try:
        age = int(input("WHAATTTT..... is your age?"))
    except ValueError:
        print("Please type in an integer.")
    else:
        break
if age >= 16:
    print("You are old enough to legally drive.")
else:
    print("You are NOT old enough to legally drive.")