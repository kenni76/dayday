x = int(input('Введите количество людей: '))  #Задание 1
y = int(input('Введите количество шаурмы: '))
m = (y // x)
n = (y % x)
print(' Количество шаурмы,которое достанется каждому: ', m )
print('Количество шаурмы,которое пойдёт в холодильник: ', n )



from itertools import combinations #Задание 2

chislo = []
zxc = int(input('Введите первую цифру трёхзначного числа: '))
xcv = int(input('Введите вторую цифру трёхзначного числа: '))
cvb = int(input('Введите третью цифру трёхзачного числа: '))
chislo.append(zxc)
chislo.append(xcv)
chislo.append(cvb)
bvc = combinations(chislo, 3)
for i in list(bvc):
    print(i)



start = 600 #Задание 3
gotovka = 120
uborka = 240
stirka = 90
ytu = (start + uborka + stirka + gotovka)
hgf = '{:02d}:{:02d}'.format(*divmod(ytu, 60))
print(hgf)

qwer = (input('Введите пароль: ')) #Задание 4
qwerty = (input('Повторите введёный пароль: '))
if qwer == qwerty:
    print('Пароль принят')
else:
    print('Пароли не совпадают!')



jhgf = int(input('Введите первое число: '))  #Задание 5
hgfa = int(input('Введите второе число: '))
if jhgf > hgfa:
    print('Число', jhgf ,'больше числа ', hgfa )
if hgfa > jhgf:
    print('Число' , hgfa , 'больше числа ' , jhgf)
else:
    print('Числа равны')



ytrr = int(input('Введите свой возраст: ')) #Задание 6
if ytrr >= 18:
    print('Доступ разрешён')
else:
    print('Доступ запрёщён')



chislooo = []  #Задание 7
zxccc = int(input('Введите первую цифру : '))
xcvcc = int(input('Введите вторую цифру : '))
cvbcc = int(input('Введите третью цифру : '))
chislooo.append(zxccc)
chislooo.append(xcvcc)
chislooo.append(cvbcc)
print(max(chislooo))



count = 0  #Задание 8
sum = 0
chisloooo = []
zxcccc = int(input('Введите первую цифру : '))
xcvccc = int(input('Введите вторую цифру : '))
cvbccc = int(input('Введите третью цифру : '))
rtyuuu = int(input('Введите четвёртую цифру: '))
chisloooo.append(zxcccc)
chisloooo.append(xcvccc)
chisloooo.append(cvbccc)
chisloooo.append(rtyuuu)
for i in chisloooo:
    if i % 2 == 1:
        count += 1
        sum += i
print('Количество нечётных чисел: ' , count)
print('Сумма нечётных чисел: ' , sum)












