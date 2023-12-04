# Write a Python function to check whether a number is perfect or not.

num = int(input("Enter a Number : "))
div = 0

for i in range(1, num):
    if num % i == 0:
        div += i

if div == num:
    print(f"{num} is a Perfect Number.")
else:
    print(f"{num} is not a Perfect Number.")
