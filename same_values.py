
#Write a function named same_values() that takes two lists of numbers of equal size as parameters.

#The function should return a list of the indices where the values were equal in lst1 and lst2.

#For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst


#Uncomment the line below when your function is done
#print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#In this solution, we used a loop that iterates using the range of the len of our list. This 
# generates the indices we need to iterate through. Note that we assume the lists are of equal 
# size. We then access the element at the current index from each list using lst1[index] and lst2[index]. 
# If they are equal we add the index to the new list. Finally, we return the results.


