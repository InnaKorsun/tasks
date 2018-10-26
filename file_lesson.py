from la_la_song import sing
from Person import Person

file_pr = "october"
#записываем песню ла ла
def lala_file():
    output_file = open ("song.txt",'w')
    output_file.write(sing(3,3,1))
    output_file.close()

#записываем песню с менеджером контекста
def lala_file_men():
    with open("song.txt",'w') as f:
        f.write(sing(3,3,1))

#записваеи персон
def person_file():
    file_sec = open("Person.py",'r')
    out = file_sec.read()
    file_th = open("person.txt",'w')
    file_th.write(out)
    file_sec.close()
    file_th.close()

#записываем и добавляем знак восклицания в конце
def file_znak():
    output_file = open("song.txt",'r')
    for i in output_file():
        print(i + "!")


#Записываем “Number: строка из файла” из одного файла в другой
def file_number_string():
    output_file = open('song.txt','r')
    with open ('number_file','w') as file_num:
        j = 1
        for i in output_file:
            file_num.write(str(j) +":" + i)
            j+=1

#Записываем “Number: строка из файла” из одного файла в другой (print)
def file_number_string_print():
    output_file = open('song.txt','r')
    with open ('number_file','w') as file_num:
        j = 1
        for i in output_file:
            print(str(j) + ":" + i, file = file_num)
            j+=1

#Записывает в новый файл все слова в алфавитном порядке из другого файла с
#текстом. Каждое слово на новой строке.
#* (доп.) Рядом со словом укажите сколько раз
def file_abc(file_pr):
    f = open(file_pr,'r')
    list_word = []
    dict_word = {}
    for line in f:
        for word in line.split():
            list_word.append(word.lower())
    list_sort = sorted(list_word)
    for i in list_sort:
        if i in dict_word:
            dict_word[i] += 1
        else:
            dict_word[i] = 1
    with open ('abc_file','w') as file_abc:
        for key,value in dict_word.items():
            file_abc.write('{}:{}\n'.format(key,value))
        f.close()

#Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата (В первой строке заголовки
#колонок)
# Посчитайте сколько отделов на фирме
# Определите максимальную зарплату
# Определите максимальную зарплату в каждом отделе
# Выведите «Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой» в
#новый файл
#Подсказка: используйте словари.

def firma():
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

if __name__ == "__main__":

    file_number_string()
    file_number_string_print()
    file_abc(file_pr)
    firma()
