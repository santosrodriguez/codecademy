#Create a function named add_greetings() which takes a list of strings named names as a parameter.

#In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.

#Return the new list containing the greetings.


def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list



#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#First, we set up our function to accept the list of strings and we initialized a new list of strings to hold our greetings. We iterate through each name and we append and concatenate the strings at the same time within our loop. Finally, we return the list containing all of our eloquent greetings.