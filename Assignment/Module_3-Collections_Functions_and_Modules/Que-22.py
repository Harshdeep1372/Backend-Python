# Write a Python program to check whether an element exists within a tuple.

Tuple = (1, 2, 3, 4, 5)

n = int(input("Enter an Element to Check: "))

if n in Tuple:
    print(f"{n} Exists in The Tuple.")
else:
    print(f"{n} Does Not Exist in The Tuple.")

