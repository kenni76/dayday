with open('inside.txt') as d:
    text = d.read()

def function(cor, i):
    if i == '^':
        return (cor[0], cor[1] + 1)
    elif i == 'v':
        return (cor[0], cor[1] - 1)
    elif i == '>':
        return (cor[0] + 1, cor[1])
    elif i == '<':
        return (cor[0] - 1, cor[1])

day = set()
day.add((0,0))
santa = (0,0)
robot = (0,0)

for c, i in enumerate(text):
    if c%2 == 0:
        robot = function(robot, i)
        day.add(robot)
    else:
        santa = function(santa, i)
        day.add(santa)

naf = (len(day))
naruto = open('outside2', 'w')
naruto.write(str(naf))

naruto.close()
d.close()










