# Write a Python program to find the second smallest number in a list.

l1=[3,4,2,1,1,5,8,9,10,11]

l=list(set(l1))

if len(l) < 2:
    print("There is no second smallest element in the list.")
else:
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
print("Second smallest Number in List is :",l[1])
print(l)
