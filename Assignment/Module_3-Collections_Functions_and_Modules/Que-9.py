'''
Write a Python function that takes two lists and
returns true if they have at least one common member.
'''

def Equal(A, B):
    c = "Common Element Not Found"

    for i in A:
        for j in B:
            if i == j:
                c="Common Element Found"
                return c
    return c


A=list()
B=list()
n1=int(input("Enter The Size of The First List : "))
for i in range(int(n1)):
	k=int(input(f"Enter The [{i+1}] Element of First List : "))
	A.append(k)

print("First List :",A)
	
n2=int(input("\nEnter The Size of The Second List : "))
for i in range(int(n2)):
	k=int(input(f"Enter the [{i+1}] Element of Second List : "))
	B.append(k)

print("Second List :",B)
print("\nDisplay Result =",Equal(A, B))
