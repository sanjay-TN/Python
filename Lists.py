#lists
items=["bru","sugar","milk","bru2"]
print(items) #to print list items

#Accessing list elements 
print(items[-1]) #prints last element of list
print(items[2])

#modifying lists

items.pop()  #it deletes last list item
print(items)

items.append("moms magic") #it adds new item to list at last index
print(items)

items.insert(1, "spoon") #it adds new item to list at a specific location
print(items)

items.remove("sugar") #to remove an element from list
print(items)

# items.clear() #clears entire list
# print(items)

items[0]="coffe powder" #to assign new value to a list
print(items)


#Slicing Lists[start:stop:step]
# used to extract portion of a list

print(items[0:3]) # to access list from 0th index to 2nd index

print(items[0 : : 2]) #to access list from 0th index to end by skipping one element

#commom functions of lists

print(len(items)) # prints length of the string

items2=[1,21,223,222,0]
print(sorted(items2)) #used to sort the list

rev=items2.reverse() #used to reverse a list
print(items2)

items3=[2,3,4,3,2]
print(sum(items3)) # used to print sum of the given lists

print(items.index("milk")) # used to access index of lists

print(items3.count(2)) # used to count the number of perticular elements present in a list

# MATRIX (nested lists)

m=[[1,2,],
   [3,4]]
print(m)
print(m[0][1])# accessing matrix elements

