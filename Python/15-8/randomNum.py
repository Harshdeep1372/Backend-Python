import random

#print(random.randint(1,100))
#print(random.choice([10,56,89,"tops",true,"harsh",1.1,2.2]))

l=[]
lucky=[]

for i in range (1,101):
    l.append(i)

print(l)

for i in range(10):
        num= random.choice(l)
        lucky.append(num)
        l.remove(num)
print(l)
print(lucky)
   
