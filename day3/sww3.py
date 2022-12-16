import numpy as np

def f(n):
    cube_coren = (2*n + 1) ** (1 / 3)
    s = ((n -1) / (n**2 -5*n + 6)) + cube_coren
    return s

a, b, h = map(int, input().split())      #a должно быть >3(деление на 0),не знаю,нужно ли было писать обработчик ошибок или условие на a(>3)
qwe = np.arange(a, b + 1, h)
for n in qwe:
    y = f(n)
    list = []
    list.append(y)
    array2 = np.array(list)
    print(array2)



