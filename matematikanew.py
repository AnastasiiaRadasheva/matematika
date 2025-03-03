from random import randint

bebe = int(input('Sisesta tase (1, 2, 3): '))
tasadejctvia = randint(1, 2)  
tasavariant = randint(1, 4)   
tasavariant3 = randint(1, 2)  
total_questions = 0
correct_answers = 0

while True:
    if bebe < 1 or bebe > 3:
        print('Ne pravilnoe chislo')
        break

    total_questions += 1  

    if bebe == 1:
        num = randint(1, 10)
        num1 = randint(1, 10)

        if tasadejctvia == 1:
            taseotv0 = num - num1
            try:
                vastustase1 = int(input(f'{num} - {num1} = ? '))
                if taseotv0 == vastustase1:
                    correct_answers += 1  
                    print('Molodets!, napishi 666 dlja zakritija')
                elif vastustase1 == 666:
                    break
                else:
                    print('Ne pravilno, napishi 666 dlja zakritija')
            except ValueError:
                print("Pojaluysta, vvedite chislo.")

        elif tasadejctvia == 2:
            taseotv0 = num + num1
            try:
                vastustase1 = int(input(f'{num} + {num1} = ? '))
                if taseotv0 == vastustase1:
                    correct_answers += 1
                    print('Molodets!, napishi 666 dlja zakritija')
                elif vastustase1 == 666:
                    break
                else:
                    print('Ne pravilno, napishi 666 dlja zakritija')
            except ValueError:
                print("Pojaluysta, vvedite chislo.")

    elif bebe == 2:
        num2 = randint(1, 20)
        num3 = randint(1, 20)

        if tasavariant == 1:
            taseotv1 = num2 - num3
            operator = "-"
        elif tasavariant == 2:
            taseotv1 = num2 + num3
            operator = "+"
        elif tasavariant == 3:
            taseotv1 = num2 * num3
            operator = "*"
        elif tasavariant == 4:
            if num3 == 0:
                print('Delit na nol\' nelya!, napishi 666 dlja zakritija')
                continue
            taseotv1 = num2 / num3
            operator = "/"

        try:
            vastustase2 = float(input(f'{num2} {operator} {num3} = ? '))
            if round(taseotv1, 2) == round(vastustase2, 2):
                correct_answers += 1
                print('Molodets!, napishi 666 dlja zakritija')
            elif vastustase2 == 666:
                break
            else:
                print('Ne pravilno, napishi 666 dlja zakritija')
        except ValueError:
            print("Pojaluysta, vvedite chislo.")

    elif bebe == 3:
        num2 = randint(1, 100)
        num3 = randint(1, 100)

        if tasavariant3 == 1:
            taseotv1 = num2 * num3
            operator = "*"
        elif tasavariant3 == 2:
            if num3 == 0:
                print('Delit na nol\' nelya!, napishi 666 dlja zakritija')
                continue
            taseotv1 = num2 / num3
            operator = "/"

        try:
            vastustase2 = float(input(f'{num2} {operator} {num3} = ? '))
            if round(taseotv1, 2) == round(vastustase2, 2):
                correct_answers += 1
                print('Molodets! napishi 666 dlja zakritija')
            elif vastustase2 == 666:
                break
            else:
                print('Ne pravilno napishi 666 dlja zakritija')
        except ValueError:
            print("Pojaluysta, vvedite chislo.")

if total_questions > 0:
    percentage = (correct_answers / (total_questions-1)) * 100 
    if percentage < 60:
        hinne = 2
    elif 60 <= percentage < 75:
        hinne = 3
    elif 75 <= percentage < 90:
        hinne = 4
    else:
        hinne = 5

    print('--------------------------------------')
    total_questions-=1
    print(f'Teie tulemus: {correct_answers}/{total_questions} ({percentage}%)')
    print(f'Hinne: {hinne}')
    print('--------------------------------------')
else:
    print('Test ei olnud sooritatud.')

