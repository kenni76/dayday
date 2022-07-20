with open('input.1.txt') as k:
    text = k.read()

num = 0
for i in text:
    if i == '(':
        num += 1
    elif i == ')':
        num -= 1

kakashi = open('output1', 'w')
otvet = str(num)
kakashi.write(otvet)

k.close()
kakashi.close()




















