# Write a Python program to returns sum of all divisors of a number

def divisors(num):
    Sum = 0
    for i in range(1, num+1):
        if num % i == 0:
            Sum += i
    return Sum

num = int(input("Enter a number : "))

result = divisors(num)

print(f"The sum of divisors of {num} is : {result}")
print(f"Maximum number: {max_value}")
print(f"Minimum number: {min_value}")
