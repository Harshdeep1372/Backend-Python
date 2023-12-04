# Write a Python program to find the repeated items of a tuple.

T = (1, 2, 3, 2, 4, 5, 6, 4)

seen = []
duplicates = []

for i in T:
    if i not in seen:
        seen.append(i)
    else:
        duplicates.append(i)

if duplicates:
    print("Repeated items in the tuple:", duplicates)
else:
    print("No repeated items found in the tuple.")
                                
