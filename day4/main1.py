import hashlib

with open('yt.txt') as f:
    dr = f.read()

chislo = 1
while True:
    cicl = hashlib.md5((dr + str(chislo)).encode()).hexdigest()
    if cicl[:6] == '000000':
        break
    chislo += 1
print(chislo)

obc = open('otput41','w')
obc.write(str(chislo))

f.close()
obc.close()
