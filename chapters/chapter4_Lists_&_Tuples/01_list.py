#List Index
"""------------------------------------------"""
a = [1, 2, 4, 56, 6] #Creating a list using []

print(a)#Print the lising using print() function
print(a[0]) # to get first index number

a[0] = 98 #replace index 0[1] with 0[98]
print(a)

#create a list with different data type
c = [24, "Salin", False, 5.6]
print(c)


"""------------------------------------------"""
# List Slicing
"""------------------------------------------"""
anime = ["Naruto", "Attack on Titan", "Jujutsu Kaisen", "Classroom of the Elite", "Bleach", "Black Clover", "Dororo", 86] #list of anime 
print(anime)
print(anime[0:4]) #only print first 4 character/list
print(anime[-4:])


"""------------------------------------------"""
# List Methods
"""------------------------------------------"""
        # Consider the following list

l1 = [1, 8, 7, 2, 21, 15]
print(l1)

#l1.sort(): update the list to [1, 2, 7, 8, 15, 21]
l1.sort()
print(l1)


#l1.reverse(): update the list to backword/reverse
l1.reverse()
print(l1)

#l1.append(8): add 8 at the end of the list
l1.append(8)
print(l1)

#l1.insert(3, 5): add the 8 at 3 index
l1.insert(3, 5)
print(l1)

#l1.pop(2): will delete element at index 2 and return it's value
l1.pop(3)
print(l1)

#l1.remove(8): will remove 8 from the list - first number
l1.remove(8)
print(l1)