with open('iinput.txt') as s:
    dr = s.read()

day = set()
day.add((0,0))
cor = (0,0)
for i in dr:
    if i == '^':
        cor = (cor[0], cor[1] + 1)
    if i == 'v':
        cor = (cor[0], cor[1] - 1)
    if i == '>':
        cor = (cor[0]+1, cor[1])
    elif i == '<':
        cor = (cor[0] - 1, cor[1])
    day.add(cor)
d = len(day)

itachi = open('output1', 'w')
itachi.write(str(d))

itachi.close()
s.close()



