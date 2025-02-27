# Loop is a programmimg structure that repeats a set of instructions as long as a specified condition is True.Python has WHILE and FOR loops
# The Whhile Loop (in python, the while loop allows you to repeatedly execute a block of code as long  as the condition is true.
'''
SYNTAX FOR WHILE
WHILE condition:
    code to execute while
'''
i=1
while(i<=10):
    print(i)
    i=i+1

# To print only even numbers,
i=1
while(i<=10):
    if i%2!=0:
        i=i+1
        continue
    print(i)
    i=i+1
    if i>10:
        break
print("i is greater than 10")

# Nested while loop
i=0
while(i<=10):
    x=0
    while(x<i):
        print("Sanjay",end=" ")
        x+=1
    print(" ")
    i+=1

# sample work on while
password = "1234"
trials=1
while trials<3:
    while(trials<=3):
        pswd = input(f"Enter password {trials}: ")
        trials+=1
        if password == pswd:
            print("correct")
            
            break
        else:
            print("incorrect")
        
# Real world prooblem using loop bus ticket problem 
bus_seats=8
booked_seat=int(input("Enter number of seats to be booked : "))
while True:
    print("seats are booked successfully")
    bus_seats-=booked_seat
    print("remaining seats are:",bus_seats)
    break
while(bus_seats!=0):
    booked_seat=int(input("Enter number of seats to be booked : "))
    if(booked_seat <= bus_seats):
        print("seat booked")
        bus_seats-=booked_seat
        print("remaining seats : ",bus_seats)
    if(bus_seats == 0):
        print("seats are full")

''' 
FOR  loop: it is used to iterate over a squence (lits,tuple,string,range) and execute a block of code repeatedly for each element in the sequence.
structure of for loop
SYNTAX
for item in sequence:
    code to execute for each item in sequence
'''
cities=["banglore","mysore","anavatti","shimoga"]
for city in cities:
    print(city)

bag=["red","green","blue"]
for ball in bag:
    print(ball)


#for loop using range(start,stop,step)
for i in range(1,11):
    print(i)
    

for i in range(1,11,2):
    print(i,end=" ")
print("\n")


#looping over strings
name="SANJAY"
for letter in name:
    print(letter*2)

# To print string in form of its position numbers 
name="SANJAY"
n=1
for letter in name:
    print(letter*n)
    n+=1

# Output
'''
S
AA
NNN
JJJJ
AAAAA
YYYYYY 
'''
# using break in for loop
'''
the break statement is used to exit a loop early when a cretain condition met.
'''
cities=["banglore","mysore","anavatti","shimoga"]
for city in cities:
    print(city)
    break


#using continue statement in for loop 

cities=["banglore","mysore","anavatti","shimoga"]
for city in cities:
    print(city)
    continue

#using enumerate() in for loop
cities=["banglore","mysore","anavatti","shimoga"]
for index,city in enumerate(cities):
    print(f"city {index +1}: {city}")


# using else in for loop
for i in range(1,11):
    print(i)
else:
    print("ALL PRINTED")

# for loop usinf dictionary
d={"name":"sanjay",
   "age":22}
print(d.items)
for key,value in d.items():
    print(key," ",value)

# nested loops
# 2*1=2
i=2
for n in range(1,11):
    print(f"2x{n}={i*n}")

##
for i in range(2,11):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)

