#1) len of hypothenuse
a = 179
b = 971
c = (a**2 + b**2)**0.5
print(c)
#2 count 10s in number
num = int(input("Enter two digit number"))
tens = num//10
print(tens)
#3 Count sum of number
num = int(input("Enter three digit number"))
sum =num%10 + num//100 + (num//10)%10
print(sum)
#4 Print next even value
num = int(input())
if num%2==0:
    print(num+2)
else:
    print(num+1)
#5 print fractional part
num = float(input())
print("{:.3f}".format(num%1))
#6 Print first number after dot
num = float(input())
print(int((num*10)%10))
