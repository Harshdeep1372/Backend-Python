#Write a Python program to get the Factorial number of given number.

number=int(input("Enter a Integer : "))
fact=1

if number < 0:
   print("\nSorry, factorial does not exist for negative numbers")
elif number == 0:
   print("\nThe factorial of 0 is 1")
else:
   for i in range(1,number + 1):
       fact = fact*i
   print("\nThe factorial of",number,"is=",fact)

