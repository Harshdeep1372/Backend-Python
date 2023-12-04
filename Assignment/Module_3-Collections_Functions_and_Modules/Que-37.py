# Write a Python program to check multiple keys exists in a dictionary

def check(d, n):
    for i in n:
        if i not in d:
            return False
    return True

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

n = ['a', 'b', 'e']

if check(d, n):
    print("All keys exist in the dictionary.")
else:
    print("Some keys do not exist in the dictionary.")

        
