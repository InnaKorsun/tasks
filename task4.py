#Uxist triangle or not
a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
