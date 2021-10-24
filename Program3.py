""" 
This program computes the maximum number of apples that can be bought 
for a specific amount of money and displays change as well
"""

# asks user for input
moneyAmount = float(input("How much money do you have?: "))
aplPrice = float(input("Enter the price of one apple: "))

# computation
maxApples = int(moneyAmount//aplPrice)
change = moneyAmount%aplPrice

print(f"You can buy {maxApples} apples and your change is {change} pesos.")
