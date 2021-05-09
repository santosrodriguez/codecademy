weight = 41.5
premium_ground = 125.00

# Ground Shipping
if weight <= 2:
  cost = weight * 1.50 + 20.00
elif weight <= 6:
  cost = weight * 3.00 + 20.00
elif weight <= 10:
  cost = weight * 4.00 + 20.00
else:
  cost = weight * 4.75 + 20.00


# Need to convert the float to a string in order to concatenate it. 
print("Ground Shipping Cost: " + str(cost))
print("Premium Ground Shipping Cost: " + str(premium_ground))


# Drone Shipping
if weight <= 2:
  cost = weight * 4.50
elif weight <= 6:
  cost = weight * 9.00
elif weight <= 10:
  cost = weight * 12.00
else:
  cost = weight * 14.25

print("Drone Shipping Cost: " + str(cost))