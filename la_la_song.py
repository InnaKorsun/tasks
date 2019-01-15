#песня ла ла ла
def sing(a=3, b=3, c=0):
    cuplet  = "-".join(["la"]*b)+'\n' #формируем ла ла строку с
    text =cuplet*a # формируем a строк
    text = text.strip()# удаляем последний перенос строки
    text = text+"." # добавляем точку
    if c == 1:
        text = text.replace(".","!") # если не точка - ставим знак восклицания
    #print(text)
    return text
#sing(4,6,0)

#выводит второе по возрастанию значение из переданных аргументов.

#r = [x for x in input("Enter sequence number by split whitespace:").split()]
#def numbers (*r):
#    r = sorted(r)
##    print(r[1])
#    return r[1]
#numbers(*r)
