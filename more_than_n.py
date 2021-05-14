#Create a function named more_than_n that has three parameters named lst, item, and n.

#The function should return True if item appears in the list more than n times. The function should return False otherwise.

#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([4, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#We use the count() function to count the number of times item appears in lst. You could also do this manually by looping through lst and incrementing a variable every time you see item. We then compare the result to n.