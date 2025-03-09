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

# vriable length arguments
def add(a,b): # parameters used in function
    return a+b
c=add(1,2)  # arguments
print(c)

# we use * to add variable length-arguments. Example is given below.
#You can use *args and **kwargs to accept a variable number of arguments in a function.
def num(*n):
    return sum(n)
print(num(1,2,3,4,100))

#Example: Using **key word args
def details(**student):
    for key,value in student.items():
        print(f"{key}:{value}")
details(name="sanjay",age=22,course="Python")

# Lambda function
#A lambda function is a small anonymous function that can take any number of arguments but has only one expression.
# Syntax : lambda arguments: expression

add=lambda a,b: a+b
print(add(1,2))

# Recursion : Recursion occurs when a function calls itself. It's used to solve problems that can be broken down into smaller, similar problems.

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

# nested functions
# a function inside the function is called nested function,The inner function is only accessible within the outer function, allowing for more modular and controlled code execution.

def outer_calculate(a,b): # outer function
    def inner_add():      # inner function
        print(a+b)
    def inner_sub():      # inner function
        print(a-b)
    def inner_mul():      # inner function
        print(a*b)
    inner_add()
    inner_sub()
    inner_mul()
outer_calculate(5,2)


# example problems Lambda Function: Write a lambda function that multiplies two numbers.

mutiply = lambda a,b : a*b
print(mutiply(5,4))

#Recursive Function: Write a recursive function that calculates the sum of the first n numbers.

def sum(n):
    if n == 1:
        return 1
    return n+sum(n-1)
print(sum(5))

#Variable-Length Arguments: Write a function that accepts any number of arguments and returns their average.
def calculate_average(*args):
    total = sum(args)
    count = len(args)
    average = total / count if count != 0 else 0
    return average

# Example usage
numbers =10, 20, 30, 40, 50
average = calculate_average(*numbers)
print(f"The average is: {average}")