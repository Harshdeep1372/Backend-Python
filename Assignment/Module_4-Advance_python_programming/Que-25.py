# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

'''
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (subclass or derived class)
to inherit properties and behaviors (attributes and methods) from another class (superclass or base class).
This promotes code reusability and allows you to create a hierarchy of classes.

init : The __init__ method is a special method in Python classes, also known as the constructor.
       It is automatically called when an object of the class is created.
       The primary purpose of the constructor is to initialize the attributes of the object.
'''

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

d = Dog("Moti")
c = Cat("Popi")

print(d.speak())
print(c.speak())
