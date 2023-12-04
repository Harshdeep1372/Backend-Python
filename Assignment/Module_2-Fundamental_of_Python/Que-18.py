'''
Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead
if the string length of the given string is less than 3, leave it unchanged.
'''

s1 = input("Enter a String : ")

if len(s1) >= 3:
    if s1.endswith("ing"):
        s2 = s1 + "ly"
    else:
        s2 = s1 + "ing"
else:
    s2 = s1

print("Modified String :", s2)
