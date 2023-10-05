#-List is Group of different type of data.

l=[1,2,1.1,2.2,"tops",True,"Java",False,10,20,1,2]

print(l)
l.append(100)
print(l)
#l.clear()
#print(l)
l1=l.copy()
print(l1)
l1.append(200)
print(l1) #change only copied list
print(l) #No change in orignal list

l2=l
l2.append(300)
print(l2) #change both list
print(l)

print(l.count(0)) #count element as well as count true or false

print(l.index(1,2)) #show index no. for element store

l3=[1000,2000,3000]
l.extend(l3)

print(l)

print(l.index(10))
l.insert(5,101)
print(l)

l.pop() #By defualt last element remove
print(l)

l.pop(3)
print(l)

l.remove(10)
print(l)

l.reverse()
print(l)
