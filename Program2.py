# This program asks how many apples and oranges user wants to buy and displays total price

# Storing input in variables
numberOfApples = int(input("Enter the number of apples you want to buy: "))
numberOfOranges = int(input("Enter the number of oranges you want to buy: "))

# Price scheme
aplPrice = 20
orgPrice = 25

# Computation
aplTotalCost = numberOfApples * aplPrice
orgTotalCost = numberOfOranges * orgPrice
total = aplTotalCost + orgTotalCost

print(f"The total amount is {total}.")
