qwe = int(input('Введите целое число: '))    #Задание 1
spisok = list(range(11, 22))
spisok2 = list(range(31,40))
spisok3 = spisok + spisok2
if qwe in spisok3:
    print('Число в множестве')
else:
    print('Число не в множестве')


wer = int(input('Введите первое целое число: '))  #Задание 2
ert = int(input('Введите второе целое число: '))
spisok4 = list(range(4, 0))
spisok5 = list(range(1, 7))
spisok6 = spisok4 + spisok5
if wer and ert in spisok6:
    print('Числа в множестве')
else:
    print('Числа не в множестве')


s = float(input('Введите расстояние: '))  #Задание 3
t = float(input('Введите время: '))
v = s/t
if v < 30:
    print('Медленно')
if v > 30 and v < 60:
    print('Средне')
if v > 30:
    print('Быстро')


a = int(input())  #Задание 4
a1 = a // 100
a2 = (a // 10) % 10
a3 = a % 10
a4 = min(a1, a2, a3)
a5 = max(a1, a2, a3)
a6 = a5 - a4
if a5 - a4 == a6:
    print('Число интересное')
elif a5 - a4 > a6:
    print('Число неинтересное')


daf = str(input('Введите свой никнейм: '))  #Задание 5
if len(daf) >3 and len(daf) < 15:
    print('Никнейм принят')
if len(daf) < 3:
    print('Никнейм слишком короткий,минимум 3 символа')
if len(daf) > 15:
    print('Никнейм слишком длинный,максимум 15 символов')


xx = float(input('Введите координату x: '))  #Задание 6
yy = float(input('Введите координату y: '))
if xx > 0 and yy > 0:
    print('Точка принадлежит первой четверти')
    agff = input('Введите первую строчку: ')
    afghh = input('Введите вторую строчку: ')
    if len(agff) > len(afghh):
        print(afghh, 'Самая короткая строчка')
    if len(afghh) > len(agff):
        print(agff, 'Самая короткая строчка')
if xx < 0 and yy > 0:
    print('Точка принадлежит второй четверти')
    fayy = abs(xx)
    fb =(2 * fayy - yy)
    fbb = yy * yy
    f = fb / fbb
    print(fb)
if xx < 0 and yy < 0:
    print('Точка принадлежит третьей четверти')
    ghtt = str(input('Введите любые символы: '))
    ghttt = len(ghtt)
    hytt = ghttt ** xx
    hyttt = ghttt ** yy
    print('x = ',hytt)
    print('y = ',hyttt)
if xx > 0 and yy < 0:
    print('Точка принадлежит четвёртой чертвери')
    rtew = abs(xx)
    rteww = abs(yy)
    if rtew > rteww:
        print('Координата x большая по модулю')
    if rtew < rteww:
        print('Координата y большая по модулю')
    if rtew == rteww:
        print('Координаты равны')


bgfa = str(input('Введите любое предложение: '))  #Задание 7
bgfaa = 'кот'
if bgfaa in bgfa:
    print('В предложении есть слово кот')









