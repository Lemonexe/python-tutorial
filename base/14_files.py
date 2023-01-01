soubor = open('base/basnicka.txt', encoding='utf-8') # file handle
obsah = soubor.read() # read sync
soubor.close()
print(obsah[:100], '...')

# to reduce the .close() boilerplate, we can write
with open('base/basnicka.txt', encoding='utf-8') as soubor:
    # instead of slurping, we can iterate line in file:
    for radek in soubor:
        print(radek)
        break

with open('base/write-test.txt', mode='w', encoding='utf-8') as soubor2:
    print('wHat', file=soubor2)
