# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter 1st Number : "))

b = int(input("Enter 2nd Number : "))

c = int(input("Enter 3rd Number : "))


if a == b or b == c or c == a:
    sum = 0
else:
    sum = a + b + c
    
print("Your Total Sum Value is :",sum)
