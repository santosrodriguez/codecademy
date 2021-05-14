
# This is a 2 dimensional list with multiple lists inside a list
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# This is a 1 dimensional list
subjects = ["physics", "calculus", "poetry", "history"]

grades = [98, 97, 85, 88]

gradebook = [["phyics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Add the computer science list to the end of the gradebook list
gradebook.append(["computer science", 100])
# Add new list to the end of the gradebook list
gradebook.append(["visual arts", 93])
gradebook[5][1] = 98
# Remove the score of 85 from the poetry list
gradebook[2].remove(85)
# Add the value of Pass to the poetry list
gradebook[2].append("Pass")

print(gradebook)

# Add 2 gradebooks together and assign to a variable
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)