# oop stands for object oriented programming language
# example programs
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
