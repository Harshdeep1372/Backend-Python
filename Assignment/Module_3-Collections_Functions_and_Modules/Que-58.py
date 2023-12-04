# Write a Python program to convert degree to radian

def convert(n):
    radians = n * (3.14 / 180)
    return radians

n = float(input("Enter the degree value: "))

result = convert(n)

print(f"{n} degrees is equal to {result} radians.")
