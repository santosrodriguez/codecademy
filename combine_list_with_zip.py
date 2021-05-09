names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 65]

names_and_heights = zip(names, heights)

print(names_and_heights)

# Would output:
# <zip object at 0x7f1631e86b48>

# This zip object contains the location of this variable in our computer’s memory. 
# Don’t worry though, it is fairly simple to convert this object into a useable list by using the built-in function list():

converted_list = list(names_and_heights)
print(converted_list)


# Outputs:

# [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 65)]

# Our inner lists don’t use square brackets [ ] around the values. This is because they have been converted into tuples (an immutable type of list).