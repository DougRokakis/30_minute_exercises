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
    return numbers_equal_months.get(numbers, "nonexistent....You did not choose a number between 1 and 12.")

numbers = int(input("Please enter the number of the month (hint hint..It can only be 1-12): "))
print("The name of the month you have chosen is "+ str(numbers_for_months(numbers)) +".")