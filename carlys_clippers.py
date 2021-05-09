hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# Assign length of hairstyles list to a variable
num_of_hairstyles = len(hairstyles)

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# Add up all prices in price list together
for price in prices:
  total_price = total_price + price

average_price = total_price / num_of_hairstyles

print("Average Haircut Price: ", average_price)

new_prices = [price - 5 for price in prices]
print(new_prices)


total_revenue = 0
for i in range(0, num_of_hairstyles):
  total_revenue = prices[i] * last_week[i] + total_revenue

print("Total Revenue: ", total_revenue)

average_daily_revenue = total_revenue / 7

cuts_under_30 = [hairstyles[i] for i in range(0, num_of_hairstyles) if new_prices[i] < 30]

print(cuts_under_30)