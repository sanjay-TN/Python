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

    
