#Create a function named odd_indices() that has one parameter named lst.

#The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

#For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].


def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst


#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#In our solution, we iterate through a range of values. The function range(1, len(lst), 2) returns a list of numbers starting at 1, ending at the length of len, and incrementing by 2. This causes the loop to iterate through every odd number until the last index of our list of numbers. Using this, we can simply append the element at whatever index we are at since we know that using our range we will be iterating through only odd indices.

#Another way to do this would be to iterate through all indices and use an if statement to see if the index you’re currently looking at is odd.
