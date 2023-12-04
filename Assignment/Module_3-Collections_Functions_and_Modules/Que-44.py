# Write a Python program to find the highest 3 values in a dictionary.

d = {'a': 10, 'b': 25, 'c': 15, 'd': 30, 'e': 5}

values = list(d.values())

if len(values) < 3:
    print("Dictionary should have at least 3 values.")
    
else:
    l = []
    for _ in range(3):
        Max = max(values)
        l.append(Max)
        values.remove(Max)
        
    print("The highest 3 values are:", l)
    
