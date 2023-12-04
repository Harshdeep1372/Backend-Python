# Write a Python program to replace last value of tuples in a list.

L = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
n = 99

for i in range(len(L)):
    l1 = list(L[i])
    l1[-1] = n
    L[i] = tuple(l1)

print("List after replacing last values :", L)

