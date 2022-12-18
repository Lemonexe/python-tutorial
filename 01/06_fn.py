def zamen(slovo, pozice, novy_znak):
    """ this is the conventional docustring format """
    part1 = slovo[:pozice]
    part2 = slovo[pozice + 1:]
    return part1 + novy_znak + part2

print(zamen('kočka', 1, 'a'))

def no_return():
    """ returns the special None value """

print(no_return(), ', it is of type: ', type(no_return()))

# although I have access to upper scope variables
# ASSIGNING INSIDE FUNCTION CREATES A NEW ONE!
x = 0
a = 3
def set_x(new_val):
    print(f'a = {a} (global called inside function)') # THIS IS OK
    # print(f'x = {x}') # THIS MAKES ERROR HOWEVER
    x = new_val
    print(f'x = {x} (local shadowing)')
set_x(1)
print(f'x = {x} (global)')

# moral of the story: don't shadow! incl. parameter, its name also must not shadow
