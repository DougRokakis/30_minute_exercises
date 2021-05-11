#metric
#BMI = weight (kg)/((height(m))**2)
#imperial
#BMI = 703 x weight (lbs)/((height(in))**2)
#bmi_kgs=weight_in_kilograms/((height_in_cms/100)**2)
#bmi_lbs=703*weight_in_pounds/(height_in_inches**2)
while True:
    kilograms_or_pounds = str(input("Everyone loves knowing whether they're overweight or not, right? Do you weigh yourself in kilograms or pounds? "))
    if kilograms_or_pounds == "kilograms":
        while True:
            try:
                weight_in_kilograms = int(input("What is your weight in kilograms? "))
            except ValueError: 
                print("Please type in an integer for kilograms.")
            else:
                break
        while True:
            try:
                height_in_cms = int(input("What is your height in centimeters? "))
            except ValueError:
                print("Please type an integer for cms")
            else:
                bmi=round(weight_in_kilograms/((height_in_cms/100)**2),2)
                print("Your BMI is " + str(bmi) + ".")
                if bmi < 18.5:
                    print("You are underweight. Congratulations. You can eat whatever you want......and I hate you.")
                elif  18.5 < bmi < 24.9:
                    print("You are of a normal weight.")
                elif 25 < bmi <29.9:
                    print("You are overweight. Consider salads. They really aren't too bad.")
                else:
                    print("You are obese. Dr. McDougall is a great resource to try. I have faith in you.")
                break
        break
    elif kilograms_or_pounds == "pounds":
        while True:
            try:
                weight_in_pounds = int(input("What is your weight in pounds? "))
            except ValueError:
                print("Please type an integer for pounds.")
            else:
                break
        while True:
            try:
                height_in_feet = int(input("Please provide the feet of your height. "))
            except ValueError:
                print("Please type an integer for feet.")
            else:
                break
        while True:
            try:
                height_in_inches = int(input("Please provide the remaining inches of your height. "))
            except ValueError:
                print("Please type an integer for inches.")
            else:
                bmi=round(703*weight_in_pounds/(((height_in_feet*12)+height_in_inches)**2), 2)
                print("Your BMI is " +str(bmi)+ ".")
                if bmi < 18.5:
                    print("You are underweight. Congratulations. You can eat whatever you want......and I hate you.")
                elif  18.5 < bmi < 24.9:
                    print("You are of a normal weight.")
                elif 25 < bmi <29.9:
                    print("You are overweight. Consider salads. They really aren't too bad.")
                else:
                    print("You are obese. Dr. McDougall is a great resource to try for losing weight. I have faith in you.")
                break
        break
    else:
        print("Please make sure to type 'kilograms' or 'pounds'.")
        continue