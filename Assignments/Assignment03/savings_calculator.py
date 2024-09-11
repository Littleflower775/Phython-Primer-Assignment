money_start = input('How much money do you have? $ ')
saving_years = input('How many years do you want to save it for? ')
interest_rate = input('What is the interest rate? ')

money_result = int(money_start) * int(interest_rate) * int(saving_years)

print(f"Your savings after {saving_years} years:", '$', (money_result))
print(f"Will you be able to afford your holiday?", (money_result >= 10000))


