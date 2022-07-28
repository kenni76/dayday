d = open ('text1.txt', 'r')

def function(lenght, width, height):
    size = 2*lenght*width + 2*width*height + 2*lenght*height
    global min
    if lenght*height < lenght*width:
        if lenght*height < height*width:
            min = lenght*height
        else:
            min = height*width
    else:
        if lenght*width < height*width:
            min = lenght*width
        else:
            min = height*width
    return size + min

summa = 0
for tyn in d:
    num = tyn.split('x')
    summa += function(int(num[0]), int(num[1]), int(num[2]))

kakashik = open('input2.txt','w')
otvet = str(summa)
kakashik.write(otvet)

d.close()
kakashik.close()