# Write a Python program to read a file line by line and store it into a list

path = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example2.txt"

l = []

with open(path, 'r') as file:
    for i in file:
        l.append(i.strip())

print(l)
