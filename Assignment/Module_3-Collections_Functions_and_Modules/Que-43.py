'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.

Sample data: {'1': ['a','b'], '2': ['c','d']}

Expected Output: ac ad bc bd
'''

from itertools import product

def print(d):
    keys = list(d.keys())
    mix = product(*(d[i] for i in keys))
    
    result = [''.join(i) for i in mix]
    print(' '.join(result))


d = {'1': ['a', 'b'], '2': ['c', 'd']}


print(d)
