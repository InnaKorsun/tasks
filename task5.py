#Method 1 (buble sort)
#a = [int(x) for x in input().split()]
#for i in range(len(a),0,-1):
#    for j in range(1, i):
#        if a[j-1] > a[j]:
#            a[j-1],a[j]=a[j],a[j-1]
#print (a)

#Method 2 (works only with 3 numbers)
a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
if a>b:
    a,b = b,a
print(a,b,c)
