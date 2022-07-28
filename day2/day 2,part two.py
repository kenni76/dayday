d = open('day2.txt', 'r')

def getdominate(lenght, width, height):
    razmer = lenght*width*height
    s = (sorted([lenght, width, height]))[:2]
    minimum = s[0] * 2 + s[1] * 2
    return razmer + minimum

dominate = 0
for tyn in d:
    num = tyn.split('x')
    dominate += getdominate(int(num[0]), int(num[1]), int(num[2]))

ink = open('output1', 'w')
otvet = str(dominate)
ink.write(otvet)

ink.close()
d.close()
