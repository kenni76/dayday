import numpy as np     #Задание 1
def func(*x):
    a = []
    a.append(x)
    cv = lambda x: np.std(a, ddof=1) / np.mean(a)
    print(np.mean(a), np.var(a), np.std(a), cv(a), sep="\n")



# Задание 2
def fuunc(*c):
    list_of_str, list_of_num, list_of_bool = [], [], []
    obshee = []
    for ii in c:
        if type(ii) is str:
            list_of_str.append(ii)
        if type(ii) is int or type(ii) is float:
            list_of_num.append(ii)
        if ii is True or ii is False:
            list_of_bool.append(ii)
        obshee += list_of_num + list_of_str + list_of_bool

    list_of_other = [elem for elem in c if elem not in obshee]
    print(list_of_other, list_of_bool, list_of_num, list_of_str, sep="\n")



# Задание 3
dict1 = {'1':{'DEBUG':'Tracemod'}, '2' : {'ERROR':'Null pointer exception'}, '3' : {'INFO' :
'startGameAllert'}, '4' : {'DEBUG' : 'sendAllert'}, '5' : {'ERROR' : 'No valid JSON'}}

def funkk(key, **dictss):
    dc = dict(dictss)
    for im in dc.values():
        if key in im:
            print(im)







