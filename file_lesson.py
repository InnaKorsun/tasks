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
     #достаем все слова из файла в лист list_word
        for word in line.split():
            list_word.append(word.lower())
    list_sort = sorted(list_word)
    #формируем словарь с словами и количеством повторов
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

list_data=[] #все содержимое файла

list_zp = [] #лист всех зп фирмы

zp_dict = {} #
dict_dep_salary={} #

#переносим все содержимое файла в лист   list_data

def get_list_from_file():
    with open("table",'r') as table:
        #создаем list_data  - лист с содержим файла
        for line in table:
            line = line.rstrip('\n') #убираем символы перевода строки справа
            list_data.append(line.split())
        print(list_data)
    return list_data

#максимальная зарплата
def max_salary_company(list_data):

        # проходим циклом по строкам с людьми (за исключением первой строки с заголовками)
        #формируем list_zp - лист с зарпадами всех сотрудников на фирме
    for i in range(1,len(list_data)):
        list_zp.append(list_data[i][3])
        #print(list_zp)
        #сортируем лист с зарплатами по возрастанию - максимальный елемент - последний
    zp_max = sorted(list_zp)
    max_salary_com = zp_max[len(zp_max)-1]
    print("Max salary in company "+str(max_salary_com))
    list_zp.clear()
    return max_salary_com

 #количество отделов

def count_department(list_data):

    depart_list = []# лист всех департаментов в фирме
    count_dep = [] # лист уникальных департаментов
        # проходим циклом по строкам с людьми (за исключением первой строки с заголовками)
        #формируем depart_list - лист отделов всех сотрудников на фирме
    for i in range(1,len(list_data)):
        depart_list.append(list_data[i][2])
        #print(depart_list)
        #формируем dep_count лист с оригинальними значениями отделов
        #длина етого масива  - и есть количество отделов
    for x in depart_list:
        if x not in count_dep:
            count_dep.append(x)
    dep_count = len(count_dep)
    print("Count of department "+str(dep_count))
    return dep_count


#Определите максимальную зарплату в каждом отделе

def max_salary_in_department(list_data):

    depart_dict={} # словарь {"Department": [Last name,Name,Salary] }
        #формирование словаря {"Department": [Last name,Name,Salary] где название фепартамента  - уникально
        # проходим циклом по строкам с людьми (за исключением первой строки с заголовкам
    for i in range (1,len(list_data)):
            #проверяем если ли название департамента в ключе словаря {"Department": [Last name,Name,Salary] }
        if list_data[i][2] in depart_dict.keys():
            val = depart_dict.get(list_data[i][2])
                #если в словаре уже есть человек с департемента, добавляем его словарь({"department":[[person1],[person2]]
            val.append([list_data[i][0],list_data[i][1],list_data[i][3]])
        else:
                #если департамент встечается впервые добавляем в словарь
            depart_dict[list_data[i][2]] = [[list_data[i][0],list_data[i][1],list_data[i][3]]]

    for key in depart_dict.keys():
            #получаем всех  сотрудников в одном департаменте
        val  = depart_dict.get(key)
        for k in range(0,len(val)):
                #добавляем в list_zp все зарплаты в отделе
            list_zp.append(val[k][2])
        list_zp.sort()
            #ищем максимальную
        max_sal = list_zp[len(list_zp)-1]
        print("Department "+ key + " has max salary" +str(max_sal))
            # создаем словарь dict_dep_salary {"department": max salary} и возвращаем его
        dict_dep_salary[key] = max_sal
        list_zp.clear()
    return dict_dep_salary,depart_dict

# Выведите «Отдел Макс_Зарплата Фамилия_человека_с_такой_зарплатой» в
#новый файл
def full_info_max_salary(depart_dep_salary,depart_dict):
        #используем пары ключ значение с словаря с метода max_salary_in_department {"department": max salary}
    for i,j in depart_dep_salary.items():
            #используем словарь {{"Department"}:[person1][repson2]} где person1 = [Last name,name,salary]
        for key in depart_dict.keys():
            val  = depart_dict.get(key)
                #заходим циклом в информацию о человеке
            for k in range(0,len(val)):
                    #проверяем что департамент равен департаменту с d и зарплата человека равна максимальной (со словаря d)
                if i==key and val[k][2]==j:
                    print("In department {} max salary {} has {}".format(key, val[k][2], val[k][0]))



if __name__ == "__main__":

    #file_number_string()
    #file_number_string_print()
    #file_abc(file_pr)
    sostav = get_list_from_file()
    max_salary_company(sostav)
    count_department(sostav)
    d,c = max_salary_in_department(sostav)
    full_info_max_salary(d,c)


