# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

# Get the number of toppings and assign it to a new variable
num_pizzas = len(toppings)

print(num_two_dollar_slices)

print("We sell " + str(num_pizzas) + " different kind of pizza!")

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices.append([2.5, "peppers"])

pizza_and_prices.sort()

# Remove the last element in the list
pizza_and_prices.pop(-1)
priciest_pizza = pizza_and_prices[-1]
cheapest_pizza = pizza_and_prices[0]
# Assign from the fist to the fourth element (0-3)
three_cheapest = pizza_and_prices[:3]

print(pizza_and_prices)
print("Cheapest pizza price: " + str(cheapest_pizza))
print("Priciest pizza price: " + str(priciest_pizza))
print("The three cheapest slicest are: " + str(three_cheapest))