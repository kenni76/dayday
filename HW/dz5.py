s = int(input('Введите цифру: '))   #Задание 1
spisok = []
kdd = []

for i in range(s):
   x = str(input('введите строку: '))
   spisok.append(x)

v = (spisok[:])
for bv in v:
    nbb = (bv[0])
    kdd.append(nbb)
for vaa in range(len(kdd)):
   print(kdd[vaa], end = '')



baw = str(input('Введите: '))       #Задание 2
print(len(baw))
print(baw[0])
print(baw[-1])
print(baw[::-1])
print(baw[::2])
print(baw[1::2])



stack = input('Введите что нибудь: ')    #Задание 3
adddd = []
abbbbb = []
abeer = []
if stack.isdigit() == True:
    for ntyy in stack:
        adddd.append(int(ntyy))
    for chislochek in adddd:
        qweewq = chislochek * 10
        abbbbb.append(int(qweewq))
    for hhika in abbbbb:
        print(hhika)
if stack.isalpha() == True:
    print(stack.count('q'))
for genshin in stack:
    abeer.append(genshin)
    if stack.isprintable() == False:
        for index in stack:
            print(index)




vvedite = input('Введите что-нибудь')      #Задание 4
for ggeerrr in vvedite:
    if vvedite.isprintable() == False:
        continue
    if vvedite.isdigit() == True:
        print('Строка состоит из чисел')
    if vvedite.isalpha() == True and vvedite != 'STOP':
        print('Строка состоит из букв')
    if vvedite.isalnum() == True and vvedite.isdigit() == False and vvedite.isalpha() == False:
        print('Смешанная строка')
    if vvedite == 'STOP':
        break














