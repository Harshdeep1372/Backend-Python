import random
data=open("data.txt","w")

for i in range(10):
    data.write(str(random.randint(1,100))+",")

data.close()

data=open("data.txt","r")
even=open("even.txt","w")
odd=open("odd.text","w")

l=data.read().split(",")[:-1]
for i in l:
    if int(i)%2==0:
        even.write(i+",")
    else:
        odd.write(i+",")


data.close()
even.close()
odd.close()



