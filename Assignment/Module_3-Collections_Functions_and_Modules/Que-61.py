# Write a Python program to calculate surface volume and area of a cylinder

def volume(r, h):
    vol = 3.14 * r**2 * h
    return vol

def area(r, h):
    a = 2 * 3.14 * r * (r + h)
    return a

r = float(input("Enter the radius of the cylinder : "))
h = float(input("Enter the height of the cylinder : "))

res1 = volume(r,h)
res2 = area(r,h)

print(f"Volume of the cylinder : {res1:.2f}")
print(f"Surface Area of the cylinder : {res2:.2f}")

