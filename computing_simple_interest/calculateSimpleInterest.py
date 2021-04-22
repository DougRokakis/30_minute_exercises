def simpleInterest(principal, rate_of_interest, number_of_years):
    SI = (principal*rate_of_interest*number_of_years)/100
    return SI

principal = input("Please enter the prinicpal amount of money invested: ")
rate_of_interest = round(input("Please enter the rate of interest: "), 2)
number_of_years = input("Please enter the number of years invested: ")

SI = simpleInterest(principal, rate_of_interest, number_of_years)

print("Simple interest: {}".format(SI))