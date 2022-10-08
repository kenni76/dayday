with open('input (2).txt') as k:
    spisok = k.read().split('\n')

good = 0

for z in spisok:

    sound = 0
    sound2 = 0
    verty = 0

    for q in z:
        if q == 'a' or 'e' or 'i' or 'u' or 'o':
            sound += 1
    for i in range(len(z) - 1):
        if z[i] == z[i + 1]:
            sound2 += 1
    for qws in ['ab', 'cd', 'pq', 'xy']:
        if qws in z:
            verty += 1
    if sound >= 3 and sound2 >= 1 and verty == 0:
        good += 1

print(good)










