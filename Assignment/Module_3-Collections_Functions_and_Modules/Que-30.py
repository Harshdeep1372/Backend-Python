# Write a Python program to convert a list of tuples into a dictionary.

t = [(1, 'apple'), (2, 'banana'), (3, 'orange')]

result = {}

for i in t:
    key, value = i
    result[key] = value

print(result)
