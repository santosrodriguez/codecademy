#Create a function named twice_as_large() that has two parameters named num1 and num2.

#Return True if num1 is more than double num2. Return False otherwise.

# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > 2 * num2:
    return True
  else:
    return False

# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True


#In this function, we also performed the operation within the condition of the if statement. The second input is multiplied by 2 and then compared to the first input on the same line.