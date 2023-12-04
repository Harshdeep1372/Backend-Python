def insert(s1, s2):
    center = len(s1) // 2
    res = s1[:center] + s2 + s1[center:]
    return res

# Example usage
s1= input("Enter a Main String : ")
s2 = input("Enter The String to Insert : ")

res = insert(s1, s2)

print("New String :", res)
