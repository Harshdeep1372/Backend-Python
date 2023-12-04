# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

'''
class : class is a blueprint for creating objects.

Self :  It is refers to the instance of the class and
        When you create an instance of the class, it is passed automatically,
        and you can access the instance's attributes and methods using it.
'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

d1 = Dog(name="Moti", age=3)
d2 = Dog(name="Sheru", age=5)

print(f"{d1.name} is {d1.age} years old.")
print(f"{d2.name} is {d2.age} years old.")
