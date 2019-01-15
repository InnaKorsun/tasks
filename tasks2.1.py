try:
    st = input()
    print(st[2],
        st[-2],
        st[:5],
        st[0:-3],
        st[1::2],
        st[::2],
        st[::-1],
        st[-1::-2],
        st[-2::-2],
        len(st),
        end="\n")
except Exception as er:
    print("String too short")
