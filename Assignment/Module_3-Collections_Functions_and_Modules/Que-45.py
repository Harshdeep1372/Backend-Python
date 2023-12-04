'''
Write a Python program to combine values in python list of dictionaries.

Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, {'item': 'item1', 'amount': 750}]

Expected Output:
Counter ({'item1': 1150, 'item2': 300})
'''

from collections import Counter

def add(l):
    result = Counter()
    
    for i in l:
        item = i['item']
        amount = i['amount']
        result[item] += amount
    
    return result

l = [{'item': 'item1', 'amount': 400},
     {'item': 'item2', 'amount': 300},
     {'item': 'item1', 'amount': 750}]

output = add(l)

print(output)
