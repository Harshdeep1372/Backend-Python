# Write a Python program to count the frequency of words in a file.

path = "E:/01_BHAVIK_All_Language/PYTHON/03_Assignment/Module[4]-Advance_python_programming/example2.txt"

f={}
file=open(path,'r')
for i in file:
    words=i.split()
    for j in words:
        word=j.strip('.,!?()[]{}"\'').lower()
        if word in f:
            f[word]+=1
        else:
            f[word]=1        

print(f)
for i,j in f.items():
    print(f"{i}:{j}")
