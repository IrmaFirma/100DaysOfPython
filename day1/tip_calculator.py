# Tip Calculator 💸
# Create a program that calculates the amount each person should pay
# Including the tip
# Use the logic for the tip calculator: https://www.calculatorsoup.com/calculators/financial/tip-calculator.php

# 🚀 SOLUTION: 
print('Welcome to Tip Calculator.')

total = float(input('How much was the total bill? '))
percent = int(input('What is your tip percentage to give? 10, 12 or 15 '))
spliters = int(input('How many people are splitting the bill? '))

bill_percent = 1 + (percent/100)
bill = total * bill_percent
per_person = round(bill / spliters, 2)

print('Each person should pay {}'.format(per_person))


#Visit: litcode.net
