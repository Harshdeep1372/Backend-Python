'''
Write a Python program to combine two dictionary adding values for
common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400}
'''

from collections import Counter

def add(d1, d2):
    d3 = Counter(d1) + Counter(d2)
    result = dict(d3)
    return result

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

result = add(d1, d2)

print("Sample output:", Counter(result))
