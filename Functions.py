# A function is a re-useable block of code performs specific tasks when called,reduces redundecy.
# functon are started with def(define) keyword followed by brackets().
def greet(): # defining or creating a function with function name
    print("hello GOOD MORNING")

greet() # calling  the function
for g in range(1,11): # to print 10 times
    greet()

def friends(boy,girl): # parameters
    print(f"my friend {boy} married {girl}")

friends("vijay","vijaylaxhmi")# positionl arguments
friends(boy="prajwal",girl="sneha") # keyword arguments


def tables(num):
    for i in range(1,11):
        print(f"{num}x{i} ={num*i}")
tables(5)

# default parameter
def friends(boy,girl="suhana"): # parameters
    print(f"my friend {boy} married {girl}")
friends("sohu")

# Returning values from a function
def myfunc(num):
    return(num**2)
a=100
b=myfunc(2)
c=int(a + b)
print(c)

def fun():
    x="sanjay" #local variable (it is defined inside the function)
    print(x)
    print(y)
y="hey"  # global variable(defined outside of the function and accessible throught th program)
fun()

def Greet():
    print("THIS IS A GREETNG MSG")
Greet()

def greet_user():
    name=input("Enter your name : ")
    print(f"hey {name} welcome to python functions")
greet_user()

def add_numbers(a,b):
    return a+b
result=add_numbers(5,3)
print(f"the sum of two numbers is : {result}")