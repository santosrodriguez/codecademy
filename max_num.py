
#Create a function named max_num() that takes a list of numbers named nums as a parameter.

#The function should return the largest number in nums


def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum
	
	
	
#Write your function here
def max_num(nums):
  return max(nums)

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#There are a few different ways to accomplish this task, but the way we did it was to check 
# every element in the list and see if there is one bigger than what we currently think is 
# the biggest. If there is a bigger one, then replace it. We keep replacing the number until 
# the largest number has been found.
