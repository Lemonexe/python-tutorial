
# FOR CYKLUS
from random import randrange
for i in range(20):
    print(randrange(0, 3), end='')

print('') # just to break line..
for pozdrav in 'Ahoj', 'Hello', 'Hola', 'Hei':
    print(pozdrav + ', ', end='')
print('')

# unused parameters are usually _, which is, however, a normal name (just a convention)
for _ in range(2):
    print('I am doing this thing twice')



# WHILE CYKLUS
odpoved = input('Řekni aaa! ')
while odpoved.lower() != 'aaa':
    print('Špatně, zkus to znovu')
    odpoved = input('Řekni aaa! ')
# btw I think shadowing is not possible. When I assing to odpoved, it assigns to the upper scope variable odpoved
print(odpoved+'\n')

while True:
    print('I WILL NOT WHILETRUE, I WIL BRAEK OUT OF THIS PRISON !!!!')
    break

# continue
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(str(i+1)+str(j+1),end=' ')
    print('')
print('')

points = 0
while points < 21:
    print('points = ',points)
    answer = input('continue? y/n: ')
    if answer != 'y':
        break
    points += randrange(2, 11)
if points > 21:
    print('FAIL, final points = ',points)
elif points > 0:
    print('OK final points = ',points)
else:
    print('coward...')
input('Press Enter to continue...')
