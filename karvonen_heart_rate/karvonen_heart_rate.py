age = int(input("Please enter your age: "))
resting_pulse = int(input("Please enter your resting pulse: "))
hr_max = 220 - age
resting_hr = 170 - resting_pulse
hr_percentage = [.55, .60, .65, .70, .75, .80, .85, .90, .95]
for i in hr_percentage:
    print(str(round((resting_hr*i)+resting_pulse)) + " bpm")
print ("These are the correlating bpm's with a heart rate percentage of 55-95 accoring to your age and resting pulse.")
print ("You should try and keep your maximum heart rate below " + str(hr_max) + " when exercising.")

#for i in hr_percentage:
#    print (str(round(i*100)) +"%  |  " + str(karvonen_hr))