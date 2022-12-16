pk = int(input('Введите число: '))  #Задание 1
for i in range(1, 11):
    f = pk * i
    print(pk,end = '')
    print('*',end = '')
    print(i,end = '')
    print('=',end = '')
    print(f)



n = int(input('Введите количество чисел: '))  #Задание 2
result = sum(int(input('Введите число: ')) for i in range(n))
print(result)



while str(input('Введите слово: ')) != 'PRINT':  #Задание 3
    print('Не то ')
else:
    print('То')



while True:   #Задание 4
    dvc = float(input('Введите первое число: '))
    dvn = float(input('Введите второе число: '))
    if dvn != 0:
        print(dvc + dvn)
        print(dvc - dvn)
        print(dvc * dvn)
        print(dvc / dvn)
        continue
    if dvn == 0:
        break






