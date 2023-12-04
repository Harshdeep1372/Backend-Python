# Write a python program to sum of the first n positive integers.

num = int(input("Enter a Positive Integer : "))
    
if num <= 0:
    print("Please Enter a Positive Integer.")
else:
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print(f"The Sum of The First {num} Positive Integers is : {sum}")
