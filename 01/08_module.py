import louka
# this reads louka.py and EXECUTES AS PROCEDURE
# then all global vars are returned as louka module

print(louka.popis_stav())

import louka # the second import just returns, doesn't run procedure
print(louka.pocet_kotatek)
