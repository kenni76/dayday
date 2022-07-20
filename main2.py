with open('input.txt') as k:
    text = k.read()


num = 0
for i, b in enumerate(text):
    if b == ')':
        num -= 1
    elif b == '(':
        num += 1
    if num == -1:
        print(i)
        break

d = open('input.2', 'w')
n = str(i)
d.write(n)

d.close()
k.close()





