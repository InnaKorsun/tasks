#Slice string to 2 part(eqaul) and change these part
st = input()
if len(st) % 2 ==0:
    l = len(st)/2
else:
    l = int(len(st)/2)+1
a = st[:l]
b = st[l:]
st2 = b+a
print(st2)

