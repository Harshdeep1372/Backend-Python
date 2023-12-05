# Write a Python program to read an entire text file.

path = 'e:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/read.txt'

file = open(path, 'r')

read = file.read()

file.close()

print(read)
