euros = input("How many Euros are you exchanging for American currency?: ")
exchange_rate = input("What is the exchange rate?: ")
euros_to_american_exchange = euros * (exchange_rate*.01)
print (str(euros) + " euros at an exchange rate of " + str(exchange_rate) + " is " + str(round(euros_to_american_exchange, 2)) + " U.S. Dollars")