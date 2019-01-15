
with open("table",'r') as table:
    list_data=[]
    depart_list=[]
    count_dep = []
    list_zp = []

    for line in table:
        line = line.rstrip('\n') #убираем символы перевода строки справа
        list_data.append(line.split())

#pмаксимальная зарплата
    for i in range(1,5):
        list_zp.append(list_data[i][3])
    print(list_zp)
    zp_max = sorted(list_zp)
    print(zp_max[len(zp_max)-1])

 #количество отделов
    for i in range(1,5):
        depart_list.append(list_data[i][2])
    print(depart_list)
    for x in depart_list:
        if x not in count_dep:
            count_dep.append(x)
    print(len(count_dep))
