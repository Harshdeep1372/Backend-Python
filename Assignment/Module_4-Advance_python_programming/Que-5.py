# Write a Python program to read last n lines of a file

path = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example2.txt"

N = int(input("Enter N value : "))

with open(path, 'r') as file:
    data= file.readlines()

print(f"The following are the last {N} lines of a text file :")

for i in (data[-N:]):
    print(i, end ='')
