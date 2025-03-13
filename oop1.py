# oop stands for object oriented programming language
# example programs
# __init__() constructor :- the init method in python is used to access an object when it is created.it is called autometically when you create a new instance of class.
# purpose: it allows you to set the initial state of the object by defining its attributes.
# self: referes to  instance of the class itself,allowing to access attributes and methods within a class.
# it is automatically passed as the first argument to methods within the class.
class Human:
    def __init__(self,name):
        self.name=name

    def walk(self):
        print(f"{self.name} is walking")

sanjay = Human("sanjay")
sanjay.walk()

class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def fast(self):
        print(f"{self.brand} is fastest mobile")

    def cost(self):
        print(f"{self.brand} is the costliest mobile")

samsung = Mobile("samsung",25000)
iphone = Mobile("iphone",50000)

samsung.fast()
iphone.cost()

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(f"{self.name} is the name of the student")
        print(f"{self.marks} is the marks of the student")

sanjay = student("sanjay",50)
sujay = student("sujay",50)

sanjay.display_info()
sujay.display_info()

    
class Movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    
    def display(self):
        print(f"{self.title} is a movie having ")
        print(f"{self.rating} ratings")

k = Movie("Kantara",10)
b = Movie("Hridyam",10)
k.display()
b.display()