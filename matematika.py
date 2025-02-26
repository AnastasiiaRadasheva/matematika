
from random import *
bebe = int(input('Sisesta tase (1, 2, 3): '))
tase1 = 1
tase2 = 2
tase3 = 3
tasadejctvia = randint(1, 2)
tasavariant = randint(1, 4)
tasavariant3 = randint(1, 2)
while True:
    if bebe < 1 or bebe > 3:
        print('Ne pravilnoe chislo')
        break
    elif bebe == 1:
        num = randint(1, 10)
        num1 = randint(1, 10)
        if tasadejctvia == 1:
            taseotv0 = num - num1
            try:
                vastustase1 = int(input(f'{num} - {num1} = ? '))
                if taseotv0 == vastustase1:
                    print('--------------------------------------')
                    print('Molodets!, napishi 666 dlja zakritija')
                    print('--------------------------------------')
                elif vastustase1 == 666:
                    break
                else:
                    print('--------------------------------------')
                    print('Ne pravilno napishi 666 dlja zakritija')
                    print('--------------------------------------')
            except ValueError:
                print("Pojaluysta, vvedite chislo.")
        elif tasadejctvia == 2:
            taseotv0 = num + num1
            try:
                vastustase1 = int(input(f'{num} + {num1} = ? '))
                if taseotv0 == vastustase1:
                    print('--------------------------------------')
                    print('Molodets !, napishi 666 dlja zakritija')
                    print('--------------------------------------')
                elif vastustase1 == 666:
                    break
                else:
                    print('--------------------------------------')
                    print('Ne pravilno, napishi 666 dlja zakritija')
                    print('--------------------------------------')
            except ValueError:
                print("Pojaluysta, vvedite chislo.")
    elif bebe == 2:
        num2 = randint(1, 20)
        num3 = randint(1, 20)
        if tasavariant == 1:
            taseotv1 = num2 - num3
            try:
                vastustase2 = int(input(f'{num2} - {num3} = ? '))
                if taseotv1 == vastustase2:
                    print('--------------------------------------')
                    print('Molodets!, napishi 666 dlja zakritija')
                    print('--------------------------------------')
                elif vastustase2 == 666:
                    break
                else:
                    print('--------------------------------------')
                    print('Ne pravilno, napishi 666 dlja zakritija')
                    print('--------------------------------------')
            except ValueError:
                print("Pojaluysta, vvedite chislo.")
        elif tasavariant == 2:
            taseotv1 = num2 + num3
            try:
                vastustase2 = int(input(f'{num2} + {num3} = ? '))
                if taseotv1 == vastustase2:
                    print('--------------------------------------')
                    print('Molodets!, napishi 666 dlja zakritija')
                    print('--------------------------------------')
                elif vastustase2 == 666:
                    break
                else:
                    print('--------------------------------------')
                    print('Ne pravilno, napishi 666 dlja zakritija')
                    print('--------------------------------------')
            except ValueError:
                print("Pojaluysta, vvedite chislo.")
        elif tasavariant == 3:
            taseotv1 = num2 * num3
            try:
                vastustase2 = int(input(f'{num2} * {num3} = ? '))
                if taseotv1 == vastustase2:
                    print('--------------------------------------')
                    print('Molodets!, napishi 666 dlja zakritija')
                    print('--------------------------------------')
                elif vastustase2 == 666:
                    break
                else:
                    print('--------------------------------------')
                    print('Ne pravilno, napishi 666 dlja zakritija')
                    print('--------------------------------------')
            except ValueError:
                print("Pojaluysta, vvedite chislo.")
        elif tasavariant == 4:
            if num3 != 0:
                taseotv1 = num2 / num3
                try:
                    vastustase2 = float(input(f'{num2} / {num3} = ? '))
                    if round(taseotv1, 2) == round(vastustase2, 2):
                        print('--------------------------------------')
                        print('Molodets!, napishi 666 dlja zakritija')
                        print('--------------------------------------')
                    elif vastustase2 == 666:
                        break
                    else:
                        print('--------------------------------------')
                        print('Ne pravilno, napishi 666 dlja zakritija')
                        print('--------------------------------------')
                except ValueError:
                    print("Pojaluysta, vvedite chislo.")
            else:
                print('--------------------------------------')
                print('Delit na nol\' nelya!, napishi 666 dlja zakritija')
                print('--------------------------------------')
    elif bebe == 3:
        num2 = randint(1, 100)
        num3 = randint(1, 100)
        if tasavariant3 == 1:
            taseotv1 = num2 * num3
            try:
                vastustase2 = int(input(f'{num2} * {num3} = ? '))
                if taseotv1 == vastustase2:
                    print('--------------------------------------')
                    print('Molodets! napishi 666 dlja zakritija')
                    print('--------------------------------------')
                elif vastustase2 == 666:
                    break
                else:
                    print('--------------------------------------')
                    print('Ne pravilno napishi 666 dlja zakritija')
                    print('--------------------------------------')
            except ValueError:
                print("Pojaluysta, vvedite chislo.")
        elif tasavariant3 == 2:
            if num3 != 0:
                taseotv1 = num2 / num3
                try:
                    vastustase2 = float(input(f'{num2} / {num3} = ? '))
                    if round(taseotv1, 2) == round(vastustase2, 2):
                        print('--------------------------------------')
                        print('Molodets! napishi 666 dlja zakritija')
                        print('--------------------------------------')
                    elif vastustase2 == 666:
                        break
                    else:
                        print('--------------------------------------')
                        print('Ne pravilno napishi 666 dlja zakritija')
                        print('--------------------------------------')
                except ValueError:
                    print("Pojaluysta, vvedite chislo.")
            else:
                print('--------------------------------------')
                print('Delit na nol\' nelya!, napishi 666 dlja zakritija')
                print('--------------------------------------')
