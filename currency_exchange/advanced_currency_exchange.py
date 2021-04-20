rates = {"eur": .83457, "gbp": .72219, "cad": 1.25062, "aud": 1.29246}
print("I see that you wish to exchange your American currency. Here at Limited Exchange Express we can exchange your money for European, British, Canadian or Australian currency.")
currency_choice = str(input("If you would like to exchange for Euros type 'eur', British currency 'gbp', Canadian currency 'cad', Australian currency 'aud': "))
amount = int(input("Please provide the amount of Amerian dollars you wish to exchange: "))
exchange_amount = (rates[currency_choice])*amount
print("Based on the currency you have chosen and the amount of American currency you have provided you are owed " + str(round(exchange_amount, 2)) +".")
#print = str(amount) + " American dollars at an exchange rate of " + rates[currency_choice] + " is " + exchange_amount + " dollars in the currency of your choosing."