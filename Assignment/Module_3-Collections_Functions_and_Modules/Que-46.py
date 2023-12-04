# Write a Python program to create a dictionary from a string

s = "hello, world!"

d = {}

for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print("Dictionary : ",d)
