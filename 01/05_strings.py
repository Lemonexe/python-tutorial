print(len('Asdf'))
print("Uvozovky 'fungují' v stringu?\n\tThis one has escaped: \" using \\\"")
print(' using the \\N{name of character}: \N{GREEK CAPITAL LETTER DELTA}')

# multiline string, keeps white spaces
lyrics = '''Haló haló!
    Co se stalo?  
Prase kozu potrkalo!'''
print(lyrics)

concat = 'one' + 'two'
repeat = 'o' * 35
charAt = 'čokoláda'[5]
charAt = 'čokoláda'[-1] # last letter (1st from end)
substr = 'čokoláda'[2:4] # substring <2;4)
substr = 'čokoláda'[4:] # substring from 4 on, inclusive
substr = 'čokoláda'[4:-1] # substring <4, -1)
print('čoko' in 'čokoláda')

# most string functions are methods, just len() is global function
'Jirka'.lower() + 'Jirka'.upper()

# dump into TEMPLATE, like JS `aa ${bb} cc` 
print(f'concatted: {concat}, last char: {charAt}, substr: {substr}')

# Or a REUSABLE TEMPLATE + FORMAT()
templat = "Ahoy {jmeno}, your x = {cislo}"
print(templat) # not what we want
print(templat.format(cislo=7, jmeno="Lemonexe"))

# other things
trimmed =  '   a   '.strip()
replaced = 'asdf'.replace('as', 'qw')
