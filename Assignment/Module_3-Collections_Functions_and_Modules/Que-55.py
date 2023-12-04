# How will you set the starting value in generating random numbers?

'''
To generate random numbers with a specific starting value, you typically
use a seed value.
'''

import random

random.seed(50)

print(random.randint(1,100))
