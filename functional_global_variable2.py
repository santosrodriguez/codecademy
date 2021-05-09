'''
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

'''


#    Or by more common convention:

def profile():
    name = "Danny"
    age = 30
    return name, age
#  Keep in mind that even in the above example we are returning a tuple (despite the lack of paranthesis) and not separate multiple values.


profile_name, profile_age = profile()
print(profile_name)
# Output: Danny
print(profile_age)
# Output: 30







#If you want to take it one step further, you can also make use of namedtuple. Here is an example:

from collections import namedtuple
def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name="Danny", age=31)

# Use as namedtuple
p = profile()
print(p, type(p))
# Person(name='Danny', age=31) <class '__main__.Person'>
print(p.name)
# Danny
print(p.age)
#31

# Use as plain tuple
p = profile()
print(p[0])
# Danny
print(p[1])
#31

# Unpack it immediatly
name, age = profile()
print(name)
# Danny
print(age)
#31

#This is a better way to do it along with returning lists and dicts. Don’t use global keyword unless you know what you are doing. 
# #global might be a better option in a few cases but is not in most of them.