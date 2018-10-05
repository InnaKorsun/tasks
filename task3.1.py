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

#вывести количество донат - от 0 до 10 - количество донат - н, если больше - количество донат - мени
def donuts(count):
    try:
        if count >=0 and count<10:
            res = "Number of donats {}".format(count)
        else:
            res = "Number of donats: many"
    except NameError as er:
        print(er)
    return res
print(donuts(5))

#Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    if len(s)>=2:
        res = s[0:2]+s[-2:]
    else:
        return ""
    return res
print(both_ends("lre"))

#Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
def fix_start(st):
    if len(st)>=1:
        first = st[0]
        last = st[1:]
        last = last.replace(first,"*")
        res = first+last
    else:
        return st
    return res
print(fix_start("babble"))

#Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):
    if len(a) >2 and len(b)>2:
        res = b[0:2]+a[2:] + " " + a[0:2]+b[2:]
    else:
        return a,b
    return res
print(mix_up('dog', 'dinner'))
