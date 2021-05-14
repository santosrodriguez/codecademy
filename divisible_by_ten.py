#Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned.
#Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

#Return the count of how many numbers in the list are divisible by 10.



def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 60, 30, 35, 40, 50]))

#In this solution, we defined the function and set up our counter. We use a for loop to iterate through each number and check if its divisible by ten. If a number is divisible by another number then the remainder should be zero, so we use modulus. After the loop has finished, we return our count.