age = int(input("Please enter your age: "))
resting_pulse = int(input("Please enter your resting pulse: "))
hr_max = 220 - age
resting_hr = 170 - resting_pulse
hr_percentage = [.55, .60, .65, .70, .75, .80, .85, .90, .95]
print(": Intensity : Rate :")
print("--------------------")
for i in hr_percentage:
    hrt_rts = str(round((resting_hr*i)+resting_pulse)) + str(" bpm")
    print(hrt_rts[1])
    #nested_list = 