# first without the global variable

def add(value1, value2):
    result = value1 + value2

add(2, 4)
print(result)

# Oh crap, we encountered an exception. Why is it so?
# the python interpreter is telling us that we do not
# have any variable with the name of result. It is so
# because the result variable is only accessible inside
# the function in which it is created if it is not global.



# Now lets run the same code but after making the result
# variable global
def add(value1, value2):
    # Global variable means that we can access that variable outside the scope of the function as well.
    # In practical programming you should try to stay away from global keyword as it only makes life difficult by introducing unwanted variables to the global scope.
    global result
    result = value1 + value2

add(2, 4)
print(result)