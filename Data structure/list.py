"""List"""


numbers = [1, 2, 3, 4]
numbers.append(5)

print(numbers)

mylist = [10, "apple", 12, 13, 14]
print("_________")
print(mylist)
print(mylist[1:2])
print(mylist[:2])
print(mylist[2:])

items = ["apple", "banana", "Cherry", "orange", "kiwi", "melon", "mango"]
if "apple" in items:
    print("Yes, apple is in the fruits list")
elif "banana" in items:
    print("Yes, banana is in the fruits list")
else:
    print("fruit not found")


for x in items:
    print(x)

print("_________")
for x in items:
    if "apple" == x:
        print("Apple is Rs.100 per kg")
    elif "banana" == x:
        print("Banana is Rs.80 for dozen")
    elif "orange" == x:
        print("orange is Rs.30 per kg")
    elif "banana" == x:
        print("kiwi is Rs.280 per kg")
    else:
        print("fruit not found")
