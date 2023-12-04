# Write a Python program to remove an empty tuple(s) from a list of tuples


L = [(1, 2), (), (3, 4), (), (5, 6), (), (7, 8)]

i = 0

while i < len(L):
    if not L[i]:
        L.pop(i)
    else:
        i += 1

print("List After Removing Empty Tuples :", L)
