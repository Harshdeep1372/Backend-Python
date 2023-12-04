# Write a Python program to find the maximum and minimum numbers from the specified decimal numbers

l = [3.14, 2.71, 5.55, 1.23, 4.0]

Max = Min = l[0]

for i in l:
    if i > Max:
        Max = i
    elif i < Min:
        Min = i

print(f"Maximum number: {Max}")
print(f"Minimum number: {Min}")
