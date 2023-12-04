# Write a Python program to check a list is empty or not.

def Info(L1):
    if len(L1) == 0:
        return 0
    else:
        return 1
 

L1 = [5]
if Info(L1):
    print("The List is Not Empty")
else:
    print("Empty List")
