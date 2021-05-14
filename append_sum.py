#Write a function named append_sum that has one parameter — a list named named lst.

#The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

#For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

#Write your function here
def append_sum(lst):
  for i in range(3):
    lst.append(lst[-1] + lst[-2])
  return lst

#or

def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#In our solution, we add the numbers and append the result in one line. We add the last and second to last elements within the .append() function and we repeat this line two more times. Remember that when we use negative indices, it starts from the end of the list and goes towards the beginning of the list. You could also use a loop to solve this instead of repeating the lines.