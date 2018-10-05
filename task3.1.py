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
sing(4,6,0)

#выводит второе по возрастанию значение из переданных аргументов.

r = [x for x in input("Enter sequence number by split whitespace:").split()]
def numbers (*r):
    r = sorted(r)
    print(r[1])
    return r[1]
numbers(*r)

words =['aaa', 'be', 'abc', 'hello']
#вывести количество строк у которых первый и последний литерал одинаковый
def match_ends (words):
    count = 0
    for i in words:
        if len(i)>=2 and i[0]==i[-1]:
           count+=1
    print(count)
match_ends(words)

#отсортировать лист:первыми идут слова на х потом в алфавтином порядке
r = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
def front_x(r):
   x_list = []
   r = sorted(r)
   for i in range(len(r)-1,-1,-1):
       if r[i][0]=="x":
           x_list.append(r[i])
           r.pop(i)
   x_list = sorted(x_list)
   mix = x_list+r
   print(mix)
   return mix
front_x(r)

# отсортировать лист с тюплами  - тюплы по последнему значению
t = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
def sort_last(t):
    d = sorted(t,key=lambda tup:tup[len(tup)-1])
    print(d)
sort_last(t)

