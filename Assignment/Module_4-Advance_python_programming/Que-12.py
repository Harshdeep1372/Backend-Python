# Write a Python program to copy the contents of a file to another file.

m_file = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example2.txt"

c_file = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example4.txt"


with open(m_file,'r') as f1:
    read=f1.read()

with open(c_file,'w') as f2:
    f2.write(read)

with open(c_file,'r') as f3:
    c=f3.read()
    
print(c)
