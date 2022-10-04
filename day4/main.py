import hashlib

with open('kk.txt') as f:
    dr = f.read()

chislo = 1
while True:
    cicl = hashlib.md5((dr + str(chislo)).encode()).hexdigest()
    if cicl[:5] == '00000':
        break
    chislo += 1

obc = open('otput4','w')
obc.write(str(chislo))

obc.close()
f.close()

