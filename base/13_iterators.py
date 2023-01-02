# iterable datatypes = datatypes upon which iter() can be called
iterator = iter([1,2,3]) # creates the iteration collection
print(iterator, '\n', next(iterator), next(iterator)) # next() is special fn that advances the iterator (remembers its state)

for x in [1,2,3]: # could be rewritten using while iterator=iter([1, 2, 3]) && next(iterator) but why bother
    pass
print('')

# ENUMERATE - creates a sequence that enumerates a list - a sequence of (index, value)
dny = ['Po', 'Út', 'St', 'Čt', 'Pá', 'So', 'Ne']
enum = enumerate(dny)
print(list(enum))
# print(enum[3]) # you can't do anything with an enum, not even select elements

# but this is not completely useless!
# UNZIPPING an ENUM
for index,den in enumerate(dny, start=1):
    # the start param doesn't slice the array, it just specifies where the numbering starts
    print(f'{index}. den je {den}')
print('')

# now let's iterate parallel arrays
trpaslici = ['Prófa', 'Stydlín', 'Dřímal', 'Kejchal', 'Štístko', 'Šmudla', 'Rejpal'] # seven dwarfs like days
barvy = ['zelený', 'žlutý', 'oranžový', 'zelený', 'fialový']

for den,trpaslik,barva in zip(dny, trpaslici, barvy):
    print(f'V {den} má službu {barva} {trpaslik}')
print('')

# zip has ended when the shortest sequence (barvy) runs out, doesn't iterate through rest of dwarves
# this behaves kind of like left join
from itertools import zip_longest
for den,trpaslik,barva in zip_longest(dny, trpaslici, barvy, fillvalue='(nevím)'):
    # if I don't specify fillvalue it's None
    print(f'V {den} má službu {barva} {trpaslik}')
