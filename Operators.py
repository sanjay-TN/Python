#operators
#assignment operator
a=10
a*=100 #a=a*100
a+=100 #a=a+100

print(a)

#comparision operator
#it includes(<,>,<=,>=,==,!=)
a=10
b=20
print(a==b) #return true or false value
print(a!=b) #compares a is not equal to b 

#logical operators
#it includes Logical(and,or,not)
print(True and True) #returns tre if both conditions are true
print(True and False)
print(True or False) #returns true if one of the condition is true
print(not(True)) #it changes true to false and vice-versa

#membership operators
#used to check an element is a membere of a string or any data
a="sanjay"
b="hellosanjay"
print(("s" in a) and ("s" in b)) #returns true(because both a and b have s)

#bitwise opearators
#perform opearations on binary level on bits
#it includes(& | !)
a=10
b=20
print(a | b)

'''
basic problems on operators

1.python program to take 2 numbers from user as input and check if both numbers are greater than 10(using and)
2.at lest one of the numbers is less than 5(using or)
3.the first number is not greater than the second(using not)
'''
a=int(input("enter a number: "))
b=int(input("Enter b number: "))
print("value of a is :",int( a))
print("value of b is: ",int( b))
c=  a and b


print(c>10) # for first question (using and)

c= a or b
print(c<5) # for second question (using or)

if((a) <(b)): #for third question
    print("the first number is not greater than second number ")


c=not b
if(a<b):
    print("the first number is not greater than the second")# for third question (using not)




