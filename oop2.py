# Getters and Setters
#Definition: Getters and setters are methods that allow controlled access to an object's attributes.

class student:
    def __init__(self,name, age):
        self.__name=name
        self.__age=age

    def get_name(self): #getter method
        return self.__name
    
    def get_age(self): #getter method
        return self.__age
        
    def set_name(self,name): # setter method
        self.__name=name

    def set_age(self,age):
        if isinstance(age ,int):
            self.__age=age
        else:
            print("age must be in integer only")

    

a=student("sanjay",17)
a.set_age(21)
print(a.get_age())

#get_age() provides read-only access to __age, while set_age() enables controlled modification.


# method overloading 
# Definition: Method overloading is the ability to define multiple methods with the same name but different parameters.

class calc:
    def add(self,a,b,c=0):
        print(a+b+c)
c=calc()
c.add(1,2,3)


# method overriding
# Definition: Method overriding allows a child class to provide a specific implementation for a method that is already defined in its parent class.

class animal: #parent
    def make_sound(self):
        print("animal make sound")


class dog(animal): #child
    def make_sound(self):
        print("barks")


a=animal()
a.make_sound()
d=dog()
d.make_sound()

#super() Function
#Definition: The super() function is used in child classes to call a method from the parent class, enabling access to inherited methods or attributes

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the parent class's __init__ method
        self.breed = breed

    def sound(self):
        super().sound()  # Calling the parent class's sound method
        print(f"{self.name} barks")

# Usage
dog = Dog("Buddy", "Labrador")
dog.sound()


#abstract classes 
#Definition: An abstract class in Python is a class that cannot be instantiated directly. It can have abstract methods, which must be implemented by subclasses.

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def start_engine(self):
        pass  # Abstract method with no implementation

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

# Usage
car = Car()
car.start_engine()