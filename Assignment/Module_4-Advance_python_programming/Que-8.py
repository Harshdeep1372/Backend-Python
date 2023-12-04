# Write a python program to find the longest words.

path = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example2.txt"

f = open(path,'r')
s = f.read()

lst = s.split()

print(s)
print("\nLongest Word in a File is :",max(lst,key=len))
