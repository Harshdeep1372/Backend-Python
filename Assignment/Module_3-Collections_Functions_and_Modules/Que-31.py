# Write a Python script to sort (ascending and descending) a dictionary by value.

d = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}

ace = dict(sorted(d.items(), key=lambda item: item[1]))

dec = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Ascending Order :", ace)
print("Descending Order :", dec)

