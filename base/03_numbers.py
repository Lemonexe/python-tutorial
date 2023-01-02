# named arguments separator, end string (instead of \n)
print(1, 2, 3, 4, sep=', ', end='') 
print(1, 2, 3, 4, sep=', ', end='\n') 

# typing functions
int(3.13)
float('8.12')
str(6)

# import typically at beginning of file, but it is possible anywhere..
from math import sqrt, floor, ceil
print(sqrt(9))

# returns whole number from <0;3), so 0|1|2
from random import randrange
print(randrange(0, 3))

from math import nan as NaN
NaN == NaN # does not equal. It never does, not in Js either.
