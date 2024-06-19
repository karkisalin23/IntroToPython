# Creating a set - no repetition allowed!
empty_set = {1, 2, 3, 4, 5, 1}
print(type(empty_set))
print(empty_set)

#empty set
empty_set = set()
print(type(empty_set))
print(empty_set)

#add value in empty set
empty_set.add(4)
empty_set.add(5)
empty_set.add(6)

# Adding multiple elements
empty_set.update([7, 8, 9])

# Removing an element (will raise a KeyError if the element is not present)
empty_set.remove(4)

# Removing an element (will not raise an error if the element is not present)
empty_set.discard(10)

# Removing an element and returning it
element = empty_set.pop()

#print the empty_set values
print(empty_set)

#Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or set1.union(set2)

#print union
print(union_set)

# Checking if an element exists
if 5 in empty_set: 
    print('5 is in the set')
