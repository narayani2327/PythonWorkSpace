"""set"""


# force-assign the new values
myset1 = {"Apple", 10, "Orange", "Grapes", 20.0}
myset2 = {30.0, "Apple", 10, "Orange", 40}

# print the results
print("Union: ", myset1 | myset2)
print("Intersection: ", myset1 & myset2)
print("Difference: ", myset1 - myset2)
print("Union: ", myset1 ^ myset2)
