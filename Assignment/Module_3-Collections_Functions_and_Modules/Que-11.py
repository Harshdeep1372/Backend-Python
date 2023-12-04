'''
Write a Python function that takes a list and returns a new list with unique
elements of the first list.
'''

def unique(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return(x)


l=[]

n=int(input("Enter The No of Elements : "))

for i in range(n):
    x=int(input(f"Enter [{i+1}] Element : "))
    l.append(x)
print("The Elements The List :",l)
print("Unique Elements in The List :",unique(l))
