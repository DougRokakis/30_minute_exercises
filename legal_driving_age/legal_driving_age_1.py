while True:
    try:
        age = int(input("WHAATTTT..... is your age?"))
    except ValueError:
        print("Please type in an integer.")
    else:
        break
state = "You are old enough to drive" if age >=16 else "You are NOT old enough to legally drive."
print(state)