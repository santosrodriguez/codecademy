def top_tourist_locations_italy():
  # Variables defined within a function are only usable within said function
  first = "Rome"
  second = "Venice"
  third = "Florence"
  # We are returning a tuple (despite the lack of paranthesis) and not separate multiple values.
  return first, second, third


most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)

