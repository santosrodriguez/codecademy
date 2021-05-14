#Create a function called every_three_nums that has one parameter named start.

#The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))


#Uncomment the line below when your function is done
print(every_three_nums(91))


#We can write the body of this function in one line by nesting the range() function inside of the list() function. The range function accepts the starting number, the ending number (exclusive), and the amount to increment by.