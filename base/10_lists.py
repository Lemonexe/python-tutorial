# list can hold various types, while array only one type. This is a list:
zviratka = ['pes', 'kočka', 'kachna']
mess = [78, None, range(10), len] # really anything can be here...
print(mess)

def ls(arg):
    # see explanation below...
    print(', '.join(map(str, arg))) # join is function of the string, the delimiter, not of list!!??

ls(zviratka)

zviratka.append('želva')
# zviratka.extend(['holub', 'kapr']) # extend = concat
# pop = pop, insert ~ splice, remove, sort, clear, reverse...

zverinec = zviratka # as expected, it is byRef...
zverinec.insert(1, 'myš') # insert to index 1

ls(zviratka)

print(f'třetí zvíře je {zviratka[2]}')
print('From 2 to -1: ', end=''); ls(zviratka[2:-1]) # just like with strings...

# I can replace elements, and the number doesnt have to match (insert or delete)
zviratka[-3:-1] = ['slon', 'osel', 'kozel'] # this actually inserts a new kozel
zviratka[-3:-1] = ['ěžek'] # this actually deletes [-2] (kozel)

del zviratka # delete variable
print('Replaced: ', end=''); ls(zverinec)

print(f'počet psů: {zverinec.count("pes")}')

ls([1, 2] * 2) # not what I had in mind!! Works just like with strings

if []:
    print('[] is truthy just like in JS.')
else:
    print('[] is falsy, unlike JS!') # this.

# list() transforms range to list, or a string to list of chars
ls(list(range(7, 16)))

zviratka2 = list(zverinec) #  makes a copy (byVal)
zviratka2.pop() # pop last (želva)
zviratka2.pop(1) # pop [1] (myš)
zviratka2.remove('pes') # remove first occurence of pes
print('Mutated list2: ', end=''); ls(zviratka2)

zviratka3 = list(zverinec)
del zviratka3[1:3] # deletes <1;3) so only 1,2
print('Mutated list3: ', end=''); ls(zviratka3)

print('Copied list was not mutated: ', end=''); ls(zverinec) # želva has survived

print('Splitted: ', end=''); ls('asdf,gghjk,aa'.split(','))

import random
random.shuffle(zverinec) # it mutates
print('Randomly shuffled: ', end=''); ls(zverinec)
searching = 'želva'
if searching in zverinec:
    print(f'and {searching} is at: {zverinec.index(searching)}')
print(f'Random zvířátko: {random.choice(zverinec)}')

# obviously a 2D list
zverince = [zverinec, zviratka2]
print(zverince)
