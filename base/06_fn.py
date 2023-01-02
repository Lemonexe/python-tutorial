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

# optional args (they are a tuple)
def say_something(*args):
    print(args if args else 'Idk what to say..')
say_something()
say_something(1, 2, 3)

# function annotations - just arbitrary metadata. But they are metadata, not just a comment!
def kinetic_energy(m:'[kg]', v:'[m/s]') -> '[J]':
    return .5*m*v**2
Ek1 = kinetic_energy(7, 11)
# if there are many parameters, we can dump them from array
params = [7, 11] 
Ek2 = kinetic_energy(*params)
print(f"Ek = {Ek1} = {Ek2}")
print(kinetic_energy.__annotations__) # programmatically accessible - may be useful for code from libs?

# lambda function hell yeah!
from math import exp
p0 = 101.325 # kPa
M = 28e-3 # kg/mol
RT = 8.314 * 298 # J/mol
g = 9.81 # m/s2
pressure = lambda h: p0 * exp(-h*g*M/RT)
print("mt. everest pressure: {:.2f} kPa".format(pressure(8848)))
p0 = 200 # p0 is byRef in the lambda. this is more like JS, not like matlab
print("at thicker atmosfere: {:.2f} kPa".format(pressure(8848)))
