# Write a Python script to check if a given key already exists in a dictionary.

d = {'a': 1, 'b': 2, 'c': 3}

key = 'b'

if key in d:
    print(f'The key "{key}" exists in the dictionary.')
else:
    print(f'The key "{key}" does not exist in the dictionary.')
