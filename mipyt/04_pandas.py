# how to open data?
# python can open json, csv, or I can get it from requests, or database..
# xlwt for .xls; openpyxl for .xlsx
import pandas as pd

# like numpy has it's matrix datatype, pandas has DataFrame
actors = pd.read_csv('mipyt/res/actors.csv', index_col=None)
actors # conversion to string prettyprints the DataFrmae (just like in NumPy)

# or manual creation from array of arrays:
items = pd.DataFrame([["Book", 123], ["Computer", 2185]])
# or froma array of hashmaps, btw I made a mistake here. It will create two columns price and priue, with some NaNs
items = pd.DataFrame([{"name": "Book", "price": 123}, {"name": "Computer", "priue": 2185}])

actors.info() # some nerd stuff

# unlike NumPy the datatypes are dynamic: if I assign 0.3 to integer, it will automatically retype

birth_years = actors['birth'] # this is a Series - one column from DataFrame
birth_years # btw it has only one datatype (in DataFrame each col can have different)

# just like in NumPy we can perform arithmetics with the cols
century = birth_years // 100 + 1
birth_years > 1940
yrs = birth_years + [10, 20, 30, 40, 50, 60]

actors['name'].str.upper() # container for string operations on the Series

# selecting
yrs[2]
yrs[2:-2]
yrs[yrs > 1950]
yrs[(yrs > 1960) & (yrs < 1985)]

# basic statistics
print('Součet: ', yrs.sum())
print('Průměr: ', yrs.mean())
print('Medián: ', yrs.median())
print('Počet unikátních hodnot: ', yrs.nunique())
print('Koeficient špičatosti: ', yrs.kurtosis())

# this is like Javascript Array.map
actors['name'].apply(lambda nm: nm[::-1])

actors['alive'].apply({True: 'alive', False: 'deceased'}.get) # this is function callback, no need for lambda

# selecting whole dataframe
actors[1:-1] # select
actors[['name', 'alive']] # but this is projection (and because it has more cols it's a DataFrame not a Series)

# we should use [] only for projection, and use .loc[] for selecting
actors.loc[2]
actors.loc[2, 'birth']
actors.loc[2:4, 'birth':'alive'] # BEWARE, THIS IS <2;4>, NOT <2;4)
actors.loc[:, 'alive'] # same as actors['alive']
actors.loc[:, ['alive', 'name']] # this way I can change order. Could do the same with rows e.g. [1, 4, 3]
actors.iloc[2, 2] # using col numbers instead of col names

copy = actors.copy()
copy.index # index of rows
copy.columns # index of columns
copy.index = copy['name'] # reindex it by name instead of integer count which are default
copy = copy.sort_index() # not just view, this reorders the table by our chosen index (for faster search in future)
slozeny_klic = copy.set_index(['name', 'birth']) # if you need compound key for some reason
slozeny_klic.loc[('Terry', 1942)]

# MERGING like SQL LEFT JOIN
spouses = pd.read_csv('mipyt/res/spouses.csv', index_col=None)
actors.merge(spouses)

# btw pandas can do much more - generate random data, aggregation, groupby etc.
