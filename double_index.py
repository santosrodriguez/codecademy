
#create a function named double_index that has two parameters: a list named lst and a single number named index.

#The function should return a new list where all elements are the same as in lst except for the element at index. The element at index should be double the value of the element at index of the original lst.

#If index is not a valid index, the function should return the original list.

#For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

#double_index([1, 2, 3, 4], 2)



def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst


#Uncomment the line below when your function is done
#print(double_index([3, 8, -10, 12], 2))

#Note that this solution is careful not to modify the original input list. If we were to simply use lst[index] = lst[index] * 2 then the list that was passed into the function would be modified outside of the function as well. Creating a new list and writing the values to it prevents this from happening. We use slicing to extract the values before and after the index and we append the modified value at the index to our new list.