spisok = []
x1 = int(input('Введите первую цифру трёхзначного числа: '))
x2 = int(input('Введите вторую цифру трёхзначного числа: '))
x3 = int(input('Введите третью цифру трёхзначного числа: '))
spisok.append(x1)
spisok.append(x2)
spisok.append(x3)
miin = min(spisok)
maax = max(spisok)
fy = maax - miin
fd = maax + miin
fg = spisok[0] * spisok[1] * spisok[2]
if fy == spisok[0] + spisok[1] + spisok[2] - fd and fg > 150 and fg < 400:
    print('Число интересное')
    print('число магическое')
    hrer = input('Введите любую строку: ')
    a = len(hrer)
    b = float(input('Введите любое число: '))
    primer1 = (a - b) * (a - b)
    primer2 = a * b / 3
    primer3 = primer1 / primer2
    print(primer3)
if fy == spisok[0] + spisok[1] + spisok[2] - fd and not fg > 150 and not fg < 400:
    print('Число интересное')
    stroka = input('Введите строку')
    yt = len(stroka)
    i = ''.join(str(x) for x in spisok)
    ghh = (i / yt) * (i / yt)
    print(ghh)
if not fy == spisok[0] + spisok[1] + spisok[2] - fd and fg > 150 and fg < 400:
    print('Число магическое')
    ytyy = input('Введите строку')
    if 'маг' in ytyy:
        print('Строка заколдована')
    else:
        print('Нет эффекта')
if not fy == spisok[0] + spisok[1] + spisok[2] - fd and not fg > 150 and not fg < 400:
    print('Число обычное')





