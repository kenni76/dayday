total_step = 0       #5 задание
element_step = 0
n = 30
for i in range(1, n + 1):

    for j in range(1, n + 1):
        if i == j:
            element_step = n - i
            total_step += element_step
        else:
            element_step = 0
        print(element_step, end=' ')
    print('')
print(total_step)


import numpy as np  #Задание 3
import math
def f(x):
  d = ((0.2 * math.exp(x)) / (24 - x ** 2))
  return d
dd = np.arange(3, 4, 0.1)
for x in dd:
  y = f(x)
  print('При х= ' + str(x) + ' y равен ' + str(y))


countt = 0     #Задание 4
def f(n):
    pervoe = (1 / (n * math.log(n) ** 2))
    s = (pervoe / 5) + 10
    return s
bb = list(range(2,7))
for n in bb:
    b = f(n)
    countt += b
print(countt)





