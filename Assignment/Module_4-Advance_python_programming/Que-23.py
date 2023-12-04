# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

l = float(input("Enter the length of the rectangle: "))
w = float(input("Enter the width of the rectangle: "))

a = Rectangle(l, w)

print(f"The area of the rectangle is: ",a.area())

