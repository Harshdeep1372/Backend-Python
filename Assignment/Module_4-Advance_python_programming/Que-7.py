# Write a Python program to read a file line by line store it into a variable.

path = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example2.txt"

try:
    with open(path, 'r') as file:
        variable = file.read()
except Exception as e:
    print(f"An error occurred: {e}")

print(variable)
