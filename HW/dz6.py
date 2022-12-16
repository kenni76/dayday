import random     #Задание 1

razmer = int(input('Введите размер списка: '))
nachalo = int(input('Введите начало диапозона: '))
konec = int(input('Введите конец диапозона: '))
spisok = []
i = 0

while i < razmer:
    x = random.randint(nachalo, konec)
    spisok.append(x)
    i += 1
print(spisok)
print(max(spisok))
print(min(spisok))
spisok.sort()
print(spisok)
spisok.sort(reverse = True)
print(spisok)



razmer1 = int(input('Введите размер списка: '))        #Задание 2
spisok1 = []
b = 0
cool = 0
spisocchek = []

while b < razmer1:
    ree = random.randint(0,1)
    spisok1.append(ree)
    b += 1

print(spisok1)
print(spisok1.count(0))
print(spisok1.count(1))
for index,elem in enumerate(spisok1):
    if elem == cool:
        xwwe = (index)
        spisocchek.append(xwwe)
print(spisocchek)



spros = int(input('Введите количество элементов: '))     #Задание 3
udal = int(input('Введите число,которое нужно удалить: '))
spiisochek = []
cac = []

nb = 0

while nb < spros:
    bover = random.randint(0,9)
    spiisochek.append(bover)
    nb += 1
print(spiisochek)
try:
        while True:
            spiisochek.remove(udal)
except ValueError:
    pass

print(spiisochek)







