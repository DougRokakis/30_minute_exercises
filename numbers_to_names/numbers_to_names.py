def numbers_for_months(numbers):
    numbers_equal_months = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }
    return "The name of the month is " + numbers_equal_months.get(numbers, "You have chosen an invalid month")+"."

numbers = int(input("Please enter the number of the month (hint hint..It can only be 1-12)"))
print(str(numbers_for_months(numbers)))