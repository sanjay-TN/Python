# Sets is a collection of unique items that is un-ordered and un-indexed and sets not allows duplicate elements,sets are used to perform mathematical operations like UNION,INTERSECTION,and DIFFERENCE.
# Example

'''
We can create set by using curly braces or b using set() function
exmple 
set1=set((elements of set))
set1={elements of set}
'''
set1={1,4,3}
print(set1)#output {1,4,3} it shows that set is un-ordered.
#print(set1[1]) # Output 'set' object is not subscriptable (indexing not possible)

# Operations of sets
'''sets operations include union,intersection,difference'''
s1={1,2,3}
s2={3,4,5}
print(s1 | s2) #( | is used for union operation)
print(s1 & s2) #for intersection
print(s1 - s2) #for difference

#Methods of sets 
s1.add(5)# adds element to set
print(s1)
s1.pop() # removes a random element
print(s1)
s1.clear() # removes all elements of set
print(s1)
