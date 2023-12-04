# Write a Python function that takes a list of words and returns the length of the longest one.

def longest(l1):
    long = 0
    for i in l1:
        if len(i) > long:
            long = len(i)
            word = i
    return word

l1 = ["three", "Jane", "quick", "lesson", 'London', 'newyork','surendranagar']

res=longest(l1)

print(f"The longest word is '{res}' with length",len(res))


