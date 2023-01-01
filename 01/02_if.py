var = int(input('Enter number: '))
if var > 3:
    print('var is > 3')
elif var == 3:
    print('var is 3')
else:
    print('var is <= 3')

print('this is outside of the condition')

# available bool operators: and, or, not
print(True and not(False))

# also available bitwise (result is actually 1bit int)
print(True & ~False)

# if you are sure it is bool or 1bit int you can do xor these ways:

print('xors: ', True != False, True ^ False)

# ternary operator (equivalent to JS True ? 'big' : 'smol')
print('big' if True else 'smol')
