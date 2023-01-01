# looks pretty standard... Key can be number | string, value can be anything
slovnik = {'Jablko': 'Apple', 'Knoflík': 'Button', 'Myš': 'Mouse'}
empt = {}
print(f'jablko je ve slovníku? {"Jablko" in slovnik}, je to {slovnik["Jablko"]}')
slovnik['Pes'] = 'Dog'
slovnik['Pes'] = 'Hund'
del slovnik['Knoflík']
print(slovnik)

for key in slovnik:
    print(key, end=', ')
print('')

# like enumerate:
for key, value in slovnik.items():
    print(f'{key}: {value}', end=', ')
print('')

# constructor function is dict(), it can be used for byVal copy just like list()
slovnicek = dict(slovnik)


# dict(['a', 'b', 'c']) # throws an error!!!
dict(enumerate(['a', 'b', 'c'])) # not very useful
dict(len='délka', str='řetězec', dict='slovník') # not very useful
dict(zip(['a', 'b', 'c'], ['1', '2', '3'])) # NOW THIS IS USEFUL!!

# a few more useful methods:
slovnik.get('something') # gets None
# slovnik['something'] # because this produces an error
slovnik.keys()
slovnik.values()
slovnik.items() # actually list of tuples [(key, value), ...]

# let's try a little bit of real-life JSON
import json
import requests
page = requests.get('https://jira.zby.cz/content/UUC/app/currencies.php')

page.raise_for_status() # raise if status not 200

payload = json.loads(page.text)
print(f"1 CZK = {payload['rates']['CZK']} €")
json.dumps(payload)
json.dumps(payload, indent=2, ensure_ascii=False) # pretty print

# for YAML I'd have to install:
# python -m pip install pyyaml
