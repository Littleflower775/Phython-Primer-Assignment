money_start = float(input('How much money do you have? $ '))
saving_years = float(input('How many years do you want to save it for? '))
interest_rate = float(input('What is the interest rate? % '))

money_result = money_start * interest_rate * saving_years

print(f"Your savings after {saving_years} years:", '$', "{:.2f}".format(money_result))
print(f"Will you be able to afford your holiday?", (money_result >= 10000))


