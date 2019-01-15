#Написать функцию is_year_leap, принимающую 1 аргумент — год, и
#возвращающую True, если год високосный, и False иначе.
def year (year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        res = "False"
    else:
        res = "True"
    return res
print(year(2000))
#Функция принимает три числа a, b, c. Функция должна определить,
#существует ли треугольник с такими сторонами. Если треугольник
#существует, вернёт True, иначе False.
def triangle (a,b,c):
    if a + b > c and a + c > b and b + c > a:
        res = "True"
    else:
        res = "False"
    return res
print(triangle(3,3,53))
print(triangle(4,4,4))
#Функция принимает три числа a, b, c. Функция должна определить, существует
#ли треугольник с такими сторонами и если существует, то возвращает тип
#треугольника Equilateral triangle (равносторонний), Isosceles triangle
#(равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not
#a triangle).
def triangletype (a,b,c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            res = "Equilateral triangle"
        elif a==b or b==c or c==a:
            res = "Isosceles triangle"
        else:
            res = "Versatile triangle"
    else:
        res = "Not a triangle"
    return res
#print(triangletype(3,3,4))
