#Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не
#останется пустым
l = [3,2,9,4,7,6]
while l:
    print(l.pop(0))
print(l)

# Как сделать это же задание со строкой: напишите цикл, который выводит на экран и
#«удаляет» первый символ строки, пока она не станет пустой?
st = "linakostenko"
while st:
    print(st[0])
    line =st[1:]
    st=line
print(st)

#Напишите цикл, который выводит на экран и удаляет элементы списка от самого
#маленького до самого большого, пока он не останется пустым.
li = [3,2,9,4,7,6]
n = len(li)
for j in range(0,n-1):
    for i in range(0,n-j-1):
        if li[i] > li[i+1]:
            li[i],li[i + 1] = li[i + 1], li[i]
while li:
    print(li.pop(0))
print(li)

