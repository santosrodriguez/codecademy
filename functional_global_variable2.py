
# Useing the 'global' keyword to make variables local to a funtion global is bad practice
def profile():
    # Don’t try to use this method. I repeat, don’t try to use the above mentioned method!
    global name
    global age
    name = "Danny"
    age = 30

profile()
print(name)
# Output: Danny

print(age)
# Output: 30


#  Some try to solve this problem by returning a tuple, list or dict with the required values after the function terminates. It is one way to do it and works like a charm:

def profile():
    name = "Danny"
    age = 30
    return (name, age)

profile_data = profile()
print(profile_data[0])
# Output: Danny

print(profile_data[1])
# Output: 30




#    Or by more common convention:

def profile():
    name = "Danny"
    age = 30
    return name, age

profile_name, profile_age = profile()
print(profile_name)
# Output: Danny
print(profile_age)
# Output: 30