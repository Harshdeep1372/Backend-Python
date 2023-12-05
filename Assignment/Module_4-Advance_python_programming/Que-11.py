# Write a Python program to write a list to a file.

path = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example3.txt"

l=[10,20,30,50,1,2,3,50,70]

file=open(path,'w')
for i in l:
    file.write(str(i)+'\n')
file.close()

with open(path,'r') as file:
    read=file.read()
print(read)

