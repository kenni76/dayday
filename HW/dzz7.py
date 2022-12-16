import random
import math

x = random.sample(range(1000, 9999), 4)      #Задание 1
file = open('outpoot2','w')
file.write(str(x))
file.close()



spisook = list(range(-1,2))      #Задание 2
print(spisook)
for ii in spisook:
    if ii == 0:
        continue
    first = (ii * math.log(1 + (math.sin(ii) / ii)))
    second = (ii + math.sin(ii))
    y = first / second
file3 = open('outpoot3','w')
file3.write(y)
file3.close()

another = open('text3.txt','r',encoding='utf-8')     #Задание 3
another1 = another.read().split('\n')
iii = 0
for iii in range(1):
    if iii == 0:
        randomm = random.choice(another1)
        print(f'I recieve {randomm}')
        iii += 1
    if iii == 1:
        randomm = random.choice(another1)
        print(f'You recieve {randomm}')

another.close()















