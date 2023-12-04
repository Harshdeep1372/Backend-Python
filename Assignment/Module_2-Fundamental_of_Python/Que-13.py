# Write a Python program to count the number of characters (character frequency) in a string.
freq = {}
S = input("Enter a String : ")
    


for i in S:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
    
print("Character Frequency : ")
for i in freq:
    print(i,":",freq[i])
