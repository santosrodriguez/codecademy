
#Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

#The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

#For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.


def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True

#Uncomment the lines below when your function is done
#print(reversed_list([1, 2, 3], [3, 2, 1]))
#print(reversed_list([1, 5, 3], [3, 2, 1]))



#In this code, we iterate through each of the indices for the entire length of either of the lists (since we assume 
# the lengths are equal) and we perform a comparison on each of the elements. We get the element at the current 
# index from our first list with lst1[index] and we test it against the last index of the second list minus the 
# current index len(lst2) - 1 – index.

#That math is a little complicated — it helps to look at a concrete example. If we are given a list of 5 elements, 
# the valid indices are 0 to 4. Because of this, the last index in the second list is len(lst2) - 1, or 5 - 1 = 4. 
# Now in order to get the inverse of the position we are at in the first list, we subtract the index we are at 
# from the end of the second list. So on the first pass, we’ll compare the element at position 0 to the element 
# at position 5 - 1 - 0 = 4. On the next pass, we’ll compare the element at position 1 to the element at position 5 - 1 - 1 = 3, and so on.

#If any of the two elements are not equal then we know that the second list is not the reverse of the first list 
# and we return False. If we made it to the end without a mismatch then we can return True since the second list 
# is the reverse of the first. You could also try simplifying this code by using the python function reversed() 
# or other methods that you will learn later on such as ‘slicing’.

