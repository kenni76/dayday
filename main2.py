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
a = i
d = open('output.2', 'w')
n = str(a)
d.write(n)

d.close()
k.close()
