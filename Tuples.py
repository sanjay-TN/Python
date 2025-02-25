#tuples are like lists but tuples are immutable (non-changeable)
genders = ("Male","Female","Others")

print(genders)
# Accessing tuples
print(genders[0])
print(genders[2])

#Tuple operations
 #Concatination
tuple1=(1,2,3)
tuple2=(2,1,3)
tuple3=tuple1+tuple2
print(tuple3) #output(1,2,3,2,1,3)

#tuple repetition
tup1=(1,2)*3
print(tup1) # output(1,2,1,2,1,2)

#checking membership
print(1 in tuple1) # output True

#Tuple Methods 
# count used to count number of elements repeated 
print(genders.count("Male")) # Output 1

# index used to access index value
print(genders.index("Male"))# Output 0

#HOMEWORK ON TUPLES
tup=(1,2,3,4,5) # tuple with 5 elements
t2=(2,2,3,4) # tuple with 4 elements
print(tup)
print(tup [1]) #indexing tuple values
print(tup [3])
print(tup[1:5:2]) #slicing tuple
print(tup+t2) # concatinating 2 tuple