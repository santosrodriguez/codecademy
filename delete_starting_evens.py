#Write a function called delete_starting_evens() that has a parameter named lst.

#The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

#For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

#Make sure your function works even if every element in the list is even!

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst


#Uncomment the lines below when your function is done
#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))

#After defining our method, we use a while loop to keep iterating as long as some provided conditions are true. We provide two conditions for the while loop to continue. We will keep iterating as long as there is at least one number left in the list len(lst) > 0 and if the first element in the list is even lst[0] % 2 == 0. If both of these conditions are true, then we replace the list with every element except for the first one using lst[1:]. Once the list is empty or we hit an odd number, the while loop terminates and we return the modified list.