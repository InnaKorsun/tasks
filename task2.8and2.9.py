
#Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию
#distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2,
#y2).
#Считайте четыре действительных числа от пользователя и выведите результат
#работы этой функции.
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
def distance(x1, y1, x2, y2):
    a =((x2-x1)**2 + (y2-y1)**2)**0.5
    print("Disatance between 2 point = %f" % a)
distance(x1, y1, x2, y2)
