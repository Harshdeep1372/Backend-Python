#Write python program that swap two number with temp variable and without temp variable.

print("--------Swap_Value_With_Temp_Variable-----------\n")

n1=int(input("Enter First Value : "))
n2=int(input("Enter Second Value : "))

temp=n1
n1=n2
n2=temp

print("\nAfter Swapping First Value :",n1,"& Second Value :",n2)

print("\n\n--------Swap_Value_Without_Temp_Variable----------\n")

n1=int(input("Enter First Value : "))
n2=int(input("Enter Second Value : "))

n1=n1+n2
n2=n1-n2
n1=n1-nu2

print("\nAfter Swapping First Value :",n1,"& Second Value :",n2)
