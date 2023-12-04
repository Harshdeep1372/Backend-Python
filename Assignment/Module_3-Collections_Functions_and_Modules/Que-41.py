# Write a Python program to print all unique values in a dictionary.

def unique(d):
    d1 = []

    for i in d.values():
        if i not in d1:
            d1.append(i)

    return d1

d = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 4}

result = unique(d)

print("Unique values in the dictionary:", result)
