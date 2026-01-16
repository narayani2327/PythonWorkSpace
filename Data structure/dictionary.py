"""Dictionary"""


# define the dictionary
my_friends = {"Sandy": 25, "John": 20, "Jane": 22}

# Accessing components
print(my_friends.items())   # View all pairs
print(my_friends.keys())    # View all names
print(my_friends.values())  # View all ages
print(my_friends["Sandy"])  # Get Sandy's age -> 25

# Updating values
my_friends["Sandy"] = 30    # Change age to 30
print(my_friends.items())

my_friends.update({"Sandy": 40})  # Update method
print(my_friends.items())

# Removing items
my_friends.pop("Sandy")     # Removes Sandy specifically
print(my_friends.items())

my_friends.popitem()        # Removes the last inserted item
print(my_friends.items())

del my_friends["John"]      # Another way to delete a specific key
print(my_friends.items())
