# gin or whiskey = 1.5 oz(40% abv)
# beer = 12 oz (5% abv)
# wine = 5 oz (12% abv)
# US standard drink = 14g
while True:
    try:
        weight = int(input("I'm sorry to have to ask but what is your weight? "))
    except:
        print("Please provide an integer.")
    else:
        weight_in_grams= weight*453
        break
while True:
    try:
        gender = str(input("With things being what they are today I need to know what your gender is please. "))
    except:
        print("Please type female or male.")
    else:
        if gender == "male":
            gender = .68
            break
        elif gender == "female":
            gender = .55
            break
        else:
            print("Please ensure you type male or female")
            continue
while True:
    try:
        amount_of_drinks = int(input("How many drinks did you have? "))
    except:
        print("Please provide an amount in integer form.")
    else:
        break
while True:
    try:
        ounces_of_drinks = float(input("How many ounces of alcoholic beverage did you consume per drink? "))
    except:
        print("Please provide an integer.")
    else:
        grams_of_drinks = ounces_of_drinks*28
        break
while True:
    try:
        alcohol_by_volume = int(input("What is the amount of alcohol by volume of the drinks you consumed? "))
    except:
        print("Please provide an integer.")
    else:
        alcohol_by_volume = alcohol_by_volume/100
        break
while True:
    try:
        drank_over_hours = int(input("Over how many hours did you drink? "))
    except:
        print("Please provide an integer.")
    else:
        break

grams_of_alcohol_consumed_formula = amount_of_drinks*grams_of_drinks*alcohol_by_volume*.789
widmark_formula = (grams_of_alcohol_consumed_formula/(weight_in_grams*gender))*100-((drank_over_hours*.015))
print("Your BAC is " +str(widmark_formula)+".")
if widmark_formula > .08:
    print("It is not legal for you to drive.")
else:
    print("You are currently under the legal limit and are able to drive.")
