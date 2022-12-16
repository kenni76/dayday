import math
import numpy as np

#Задание 1
def f(x):
    fb = ((0.2 * math.exp(x)) / (24 - x ** 2)) + (0.6 * math.sqrt(x))
    return fb

a, b, h = map(int, input().split())
qwe = np.arange(a, b + 1, h)
for x in qwe:
    y = f(x)
    list = []
    list.append(y)
    array2 = np.array(list)
    print(array2)


#Задание 2
def funcc(r):
    aw = []
    if r > 0:
        aw.append('Положительное')
    else:
        aw.append('Отрицательное')
    if r - int(r) == 0:
        aw.append('Число целое')
    else:
        aw.append('Число не целое')
    if r % 2 == 0:
        aw.append('Число чётное')
    else:
        aw.append('Число не чётное')
    xqww = (len(str(r))) -1
    aw.append(xqww)

    def funccc(r):
        count = 0
        while r % 1 != 0:
            r *= 10
            count += 1
        return count
    xree = funccc(r)
    aw.append(xree)
    print(aw)


#Задание 3
def goroda(weew):
    vv,gg,hh = 'Москва','Томск','Екатеринбург'
    if weew in vv:
        print(vv)
    if weew in gg:
        print(gg)
    if weew in hh:
        print(hh)



