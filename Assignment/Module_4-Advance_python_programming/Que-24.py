# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        area = 3.14 * self.r ** 2
        return area

    def perimeter(self):
        perimeter = 2 * 3.14 * self.r
        return perimeter

radius = 5
o1 = Circle(radius)

print(f"Radius: {radius}")
print(f"Area:",o1.area())
print(f"Perimeter:",o1.perimeter())
