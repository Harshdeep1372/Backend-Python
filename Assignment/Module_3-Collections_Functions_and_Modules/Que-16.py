# write a python program to check whether a list contains a sub list.

def sub(l1, l2):
    if not l2:
        return True

    for i in range(len(l1)):
        if l1[i:i+len(l2)] == l2:
            return True

    return False

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [3, 4, 5]

if sub(l1, l2):
    print("The Sublist is Present In The Main List.")
else:
    print("The Sublist is Not Present In The Main List.")
