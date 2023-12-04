# Write a Python program to count the number of lines in a text file

path = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example2.txt"

f=open(path,'r')

s=f.readlines()

count=len(s)

print(f"The number of lines in the file is : {count}")
