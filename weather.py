# Notice that there are 3 print statements. The last statement is separate from the function because its not indented. The function runs last even though its printed second.

# By default, print statements add a new line character "behind the scenes" at the end of the string.


print("Checking the weather for you!")

def weather_check():
  print("Looks great outside! Enjoy your trip.")

print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")


weather_check()
