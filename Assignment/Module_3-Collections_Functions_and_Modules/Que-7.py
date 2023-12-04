# Write a Python program to remove duplicates from a list

L = [11, 13, 15, 16, 13, 15, 16, 11] 
print ("The list is: ",L) 

result = [] 
for i in L: 
    if i not in result: 
        result.append(i) 
 
print ("The List After Removing Duplicates : ",result)
