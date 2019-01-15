def sl(list1,list2):
    list3 = list1[:]
    count = 1
    for i in list2:
        list3.insert(count,i)
        count= count+2
    print(list3)
    return list3

list1 = [1,3,5,7]
list2=[2,4,6,8,10,12]

sl(list1,list2)
