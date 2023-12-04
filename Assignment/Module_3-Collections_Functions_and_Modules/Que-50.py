# Write a Python function that checks whether a passed string is palindrome or not

def palindrome(s):
    new = ''.join(i.lower() for i in s if i.isalnum())
    return new == new[::-1]

s = input("Enter a String : ")
result = palindrome(s)

if result:
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")

