# Write a Python program to read a random line from a file.

import random

try:
    file = open("sample.txt", 'r')
    total = file.readlines()
    
    if total:
        count = random.choice(total)
        print("Random Line :", count.strip())
    else:
        print("File is empty.")

    file.close()

except Exception as e:
    print(f"An error occurred: {e}")
