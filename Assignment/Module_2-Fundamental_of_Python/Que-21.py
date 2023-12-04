# Write a Python function to reverses a string if its length is a multiple of 4.

s=input("Enter a String : ")

if len(s)%4==0:
    print("Reversed String :",s[::-1])
else:
    print("String Length is Not Multiple of 4.")
