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

#L1.sort(): update the list to [1, 2, 7, 8, 15, 21]
l1.sort()
print(l1)

