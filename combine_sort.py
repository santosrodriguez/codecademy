#Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call. 





def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sortedList = sorted(unsorted)
  return sortedList

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#We start by combining the two lists together using + in order to get a new list. Next, in order to sort them, we use the sorted() function which returns a new sorted version of the list.