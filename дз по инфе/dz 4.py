import random
import math

N = int(input('первое число: '))       #Задание 1
a = int(input('второе число: '))
b = int(input('третье число: '))
i = 0
spisok = list(range(1, N+1))
add = []

for i in spisok:
    if i % 2 == 1 and i not in list(range(a, b+1)):
        add.append(i)
        continue
for x in reversed(add):
    print(x)



stroka = str(input('Введите слово: '))   #Задание 2
while stroka:
    if stroka == 'Лого':
        gaver = str(input('Введите второе слово: '))
        vb = len(gaver)
        print(math.log(vb))
        continue
    if stroka == 'Триго':
        bover = int(input('Введите градусы: '))
        print(math.cos(bover))
        print(math.sin(bover))
        print(math.tan(bover))
        print(math.cos(bover) / math.sin(bover))
        continue
    if stroka == 'Конец':
        break



xx = random.randint(0, 1000)  #Задание 3
bb = random.randint(0, 1000)

chisloo = int(input('Введите число: '))
if chisloo in list(range(xx,bb)) or chisloo in list(range(bb, xx)):
    print('Lucky')
else:
    print('Try again')



while True:                                    #Задание 4
    nn = int(input('Введите первое число: '))
    vv = int(input('Введите второе число: '))
    M = random.randint(nn, vv)
    for i in list(range(1, M + 1)):
        print(math.log(i))
    x = str(input('Желаете продолжить? '))
    if x == 'Y':
        continue












