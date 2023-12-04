# Write a Python program to count the occurrences of each word in a given sentence.

S = input("Enter a String : ")

l=S.split()

fre={}

for i in l:
    if i in fre:
        fre[i] += 1
    else:
        fre[i] = 1

print("Occurrences of Each Word is : ")

for i in fre:
    print(i,":",fre[i])    
