# Write a Python function to get the largest number, smallest num and sum of all from a list. 

List = []

N = int(input("Please Enter The Total Number of List Elements : "))

for i in range(1, N + 1):
    value = int(input(f"Please Enter The Value of [{i}] Element : "))
    List.append(value)

print("List :",List)
print("The Smallest Element in this List is : ", min(List))
print("The Largest Element in this List is : ", max(List))
print("Total Sum of All Element in this List is : ", sum(List))

