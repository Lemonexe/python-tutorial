# TUPLES like in TypeScript – when n is known, and each i has specific meaning

# syntax like list but w/o []
dvojice = 'Pat', 'Mat'
print(dvojice)

# Tuples are READONLY; no append, no pop, no dvojice[1:2] = 'nothing','else'
for item in dvojice:
    print(item)

# it is useful as a returnable (I like that it's readonly, enforces immutability?)
def double_a_double(arg):
    """ takes a touple with length 2, returns it doubled """
    return arg[0]*2, arg[1]*2

# btw when passing tuple as a param in-situ, just wrap w/ ()
print(double_a_double( (2,3) ))

# touples (and lists too) can be destructured :-)
num1, num2 = double_a_double( (2,3) )
num3, num4 = [1, 2]
print(num1, num2, num3, num4)

# lol
c,h,a,r = 'char'
print(c, h, a, r)

# wtf
empty = ()
uniple = (1,)

# easily listify a touple
print(list(dvojice))

# or tuplify a list
print(tuple([1, 2, 3, 4]))
