principal = int(input("Please enter the prinicpal amount of money invested: "))
rate_of_interest = round(input("Please enter the rate of interest: "), 2)
number_of_years = int(input("Please enter the number of years invested: "))
simple_interest = int((principal*rate_of_interest*number_of_years)/100)
yearly_interest = simple_interest/number_of_years
print("After " +str(number_of_years)+ " years at " +str(rate_of_interest)+ "%, the investment will be worth $" +str(simple_interest+principal)+ " with $" +str(yearly_interest)+ " yearly interest.")
