with open('input (2).txt') as k:
    spisok = k.read().split('\n')

good = 0

for z in spisok:

    good1 = 0
    good2 = 0
    notgood = 0

    for q in z:
        if q in ['a', 'i', 'o', 'u', 'e']:
            good1 += 1
    for i in range(len(z) - 1):
        if z[i] == z[i + 1]:
            good2 += 1
    for b in ['ab', 'cd', 'pq', 'xy']:
        if b in z:
            notgood += 1
    if good1 >= 3 and good2 >= 1 and notgood == 0:
        good += 1

output1 = open('out1put1','w')
output1.write(str(good))

k.close
output1.close










