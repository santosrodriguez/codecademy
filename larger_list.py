#Write a function named larger_list that has two parameters named lst1 and lst2.

#The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

#Write your function here
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([2, 5], [3, 7, 10]))


#We start by comparing the lengths of each of the lists using the len() function. This determines whether to return the last element of the first list or the second list. Notice that we use >=. This way, we know what to do if the lists have an equal length.

#In order to get the last element, we get the element at the -1 index. The negative index starts at the end of the list and works towards the start of the list.