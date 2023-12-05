# Write a Python program to append text to a file and display the text.

path = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example.txt"

file = open(path, "a")
file.write("\nHello, this is a new line!")
file.close()

file = open(path, "r")
content = file.read()

print("File content:")
print(content)

file.close()
