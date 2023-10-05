s=input("Enter String : ")

upper=0
lower=0
alpha=0
num=0
space=0
special=0

for i in s:
    if i.isalpha():
        alpha=alpha+1
    elif i.isnumeric():
        num=num+1
    elif i.isspace():
        space=space+1
    else:
        special=special+1
    if i.isupper():
        upper=upper+1
    elif i.islower():
        lower=lower+1
print("total upper case letter :", upper)
print("total lower case letter :", lower)
print("total space :", space)
print("total alphabetic :", alpha)
print("total numericals :", num)
print("total special letter :", special)
