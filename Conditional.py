# Dcision making (conditional statements) IF, IF-ELSE and ELSE  are used to perfprm different actions on diffrent conditions.

# IF statement
# it is used to test the condition if the condition is true, then the block of code under IF condition is executed
'''
SYNTAX
 if condition:
     code block to execute if the comdition is true
'''
x=10
if x%2==0:
    print(x,"is even")


'''
if else 
SYNTAX
if(condition):
    statement if the condition is true
else:
    statement if the condition is false
'''
x=101
if(x%2==0):
    print(x,"is even")
else:
    print(x,"is odd")

'''
if elif statement
SYNTAX
if(condititon1):
    statement to execute if
elif(condition2):
    statement to execute elif
else:
    statement to execute else
'''
signal=input("plese enter the color of the signal : ")
if(signal=="red"):
    print("STOP")
elif(signal=="yellow"):
    print("READY")
elif(signal=="green"):
    print("GO")
else:
    print("PLESE ENTER A VALID COLOR OF SIGNAL ONLY")

# comparision opearator in if
a=10
if(a>=5):
    print(a,"is greater than equal to 5")
else:
    print("not greater  than equal to 5")

#logical operators in if
attendence=int(input("enter attendence : "))
is_friend=True
if attendence >= 75 or is_friend:
    print("ELIGIBLE FOR EXAM")
else:
    print("NOT ELIGIBLE FOR EXAM")

# IF-ELIF -ELSE
gender=input("ENTER GNDER : ")
if(gender=="male"):
    print("You have to pay for bus ticket")
elif(gender=="female"):
    print("you have free ticket facility")
else:
    print("plese enter gender only")

# nested if statement (if inside if)
gender=input("enter gender : ")
age=int(input("enter age: ")) 
if(gender=="female"):
    print("free ticket")
else:
    if(age<=5):
        print("half ticket")
    elif(age>=50):
        print("senior cityzen")
    else:
        print("you have to pay full amount")
    