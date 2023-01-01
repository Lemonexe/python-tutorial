# RANGE is a sequence <2;10)
seq = range(2, 10)
print('this is not particularly informative: ', seq)
print('let\'s dump into a list: ', list(seq))

# third arg is a delimiter:
seq = range(16, 86, 4)
print(list(seq))
list(range(10, 1, -1))
# range(0, 1, .01) # nope, no floats

# WHAT IS IT GOOD FOR?
# low memory, you can store rly large numbers. Transforming seq into list, that takes up the memory.

print(list(seq[2:6])) # but you can select subrange however you want
print(f'is there 80? {80 in seq}, at position {seq.index(80)}') # btw .index throws an error when not found (in lists, seqs, anywhere)
import random
print(random.choice(seq))

# but seq has no mutative methods .pop(), .sort() etc
