# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 

s1 = input("Enter Fhe First String : ")
s2 = input("Enter The Second String : ")

if len(s1) >= 2 and len(s2) >= 2:
    a1 = s2[:2] + s1[2:]
    a2 = s1[:2] + s2[2:]
    print("Result:", a1+" "+a2)
else:
    print("Both Input Strings Should Have at Least 2 Characters.")
