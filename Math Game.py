from random import randint

print('Copyright (c) JulianDevs ')

print('Check out JulianDevs.github.io for more ')

ant_stykker = 100
ant_rett = 0

for i in range(ant_stykker):
    tall1 = randint(2, 12)
    tall2 = randint(2, 12)

    print('What is ' + str(tall1) + ' multiplication with ' + str(tall2) + '?')
    svar = input()

    if int(svar) == tall1 * tall2:
        print('Yes, the answer is correct ' + svar)
        ant_rett = ant_rett + 1
    else:
        print('No, the answer is ' + str(tall1 * tall2))

print('You got ' + str(ant_rett) + ' off ' + str(ant_stykker))

