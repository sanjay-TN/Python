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

# pillers of oop are abstraction,encapsulation,inheritance,polymorphism
# abstraction:- hiding the inner data showing only required data for the user

class atm:
    def __init__(self,balance):
        self.__balance=balance #private attribute
        print("current balance is :",self.__balance)

    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited {amount}. new balance :{self.__balance}")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance-=amount
            print(f"Withdraw {amount}. new balance :{self.__balance}")

        else:
            print(f"Insufficient balance, you have only {self.__balance} rupees left")

atm=atm(1000)
atm.deposit(500)
atm.withdraw(10000)

# encapsulation:- it is the wrpping of data and methods that operate on data with one calss.This protects the data from exteral interfaces and misuse,improve security and maintainability. It mailny uses private access modifier i.e(self.__vaiable)

class Database:
    def __init__(self):
        self.__storage={}

    def write(self, key, value):
        self.__storage[key] = value

    def read(self,key):
        if key in self.__storage:
            return self.__storage[key]
        else:
            print("DB item not available")
    
db=Database()
db.write("name", "sanjay")
db.write("name1", "sanj")
db.write("name2", "sujay")
print(db.read("name2"))

# Inheritance
 # Definition: Inheritance allows a class to inherit attributes and methods from another class, facilitating reuse.

class User:
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in")

class Admin(User):
    def delete_user(self, user):
        print(f"Admin {self.username} deleted user {user}")

admin = Admin("karnataka_admin")
admin.login()  # Inherited from User
admin.delete_user("user_102")  # Admin-specific method
# Here, Admin inherits from User and gains additional functionality.


# Polymorphism
# Definition: Polymorphism allows objects of different classes to be treated as objects of a common superclass, but they can behave differently depending on the object type.

class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS")

notifications = [EmailNotification(), SMSNotification()]
for notification in notifications:
    notification.send()

# Each notification type behaves differently while sharing a common interface.

