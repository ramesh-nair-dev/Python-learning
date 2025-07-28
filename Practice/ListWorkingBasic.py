lucky_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
friends = ["Jon Snow","Arthur Morgan","Kratos","Robb Stark","Arya Stark"]

# friends.extend(lucky_numbers)
# print(friends)
# print(friends.sort())
# This code demonstrates how to extend a list with another list in Python.
# It combines the `lucky_numbers` list with the `friends` list and then sorts the combined list in place.
# Note: The `sort()` method sorts the list in place and returns `None`, so printing it directly will show `None`.
# Because in the updated list we have strings and integers, the sort will not work as expected.
# To sort the list correctly, we should ensure that all elements are of the same type (either all strings or all integers).


# To add elements to a list, you can use the `append()` method.
friends.append("Ragnar Lothbrok")
print(friends)

# To insert an element at a specific position, you can use the `insert()` method.
print(friends.insert(1,"Loki"))
print(friends)

# To remove an element from a list, you can use the `remove()` method.
print(friends.remove("Arya Stark"))
print(friends)

# To pop an element from a list (remove and return it), you can use the `pop()` method.
print(friends.pop(-1))
print(friends)

# To clear all elements from a list, you can use the `clear()` method.
print(friends.clear())
print(friends)

friends.append("Jon Snow")
friends.append("Arthur Morgan")

print(friends)

print(friends.count("Jon Snow"))
# We can aslo count the number of occurrences of an element in a list using the `count()` method.

print(friends.index("Arthur Morgan"))
# We can find the index of an element in a list using the `index()` method.

print(friends.reverse())
# We can reverse the order of elements in a list using the `reverse()` method.

friends_2 = friends.copy()
# We can create a shallow copy of a list using the `copy()` method.
print(friends_2)
# This code demonstrates various list operations in Python, including extending lists, adding elements,

lucky_numbers.reverse()
print(lucky_numbers)
