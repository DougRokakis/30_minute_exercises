#(0°C × 9/5) + 32 = 32°F
#(32°F − 32) × 5/9 = 0°C

temp_convert = str(input("Press C to convert from Fahreheit to Celsius OR press F to convert from Celsius to Fahrenheit. ").lower())
print ("Your choice: " + temp_convert.upper())
if temp_convert.lower() == "c":
    while True:
        try:
            c_temp_convert = int(input("Please enter the temperature in Fahrenheit: "))
        except ValueError:
            print("Please be sure to type an integer.")
        else:
            fahr_to_cel = round((c_temp_convert-32)*(5/9), 2)
            print("The temperature in Celsius is " +str(fahr_to_cel))
            break
elif temp_convert.lower() == "f":
    while True:
        try:
            f_temp_convert = int(input("Please enter the temperature in Celsius: "))
        except ValueError:
            print("Please be sure to type an integer.")
        else:
            cel_to_fahr = round((f_temp_convert*9/5) + 32, 2)
            print("The temperature in Fahrenheit is " +str(cel_to_fahr))
            break