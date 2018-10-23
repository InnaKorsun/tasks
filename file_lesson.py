from la_la_song import sing
from Person import Person

#записываем песню ла ла
#output_file = open ("song.txt",'w')
#output_file.write(sing(3,3,1))
#output_file.close()

#записываем песню с менеджером контекста
with open("song.txt",'w') as f:
    f.write(sing(3,3,1))

#записваеи персон
#file_sec = open("Person.py",'r')
#out = file_sec.read()
#file_th = open("person.txt",'w')
##file_th.write(out)
#file_sec.close()
#file_th.close()

#записываем и добавляем знак восклицания в конце
#output_file = open("song.txt",'r')
#for i in output_file():
#    print(i + "!")

#
#output_file = open("song.txt",'w')
#output_file.write("list")

#Записываем “Number: строка из файла” из одного файла в другой
#output_file = open('song.txt','r')
#with open ('number_file','w') as file_num:
#    j = 1
#    for i in output_file:
#        file_num.write(str(j) +":" + i)
#        j+=1

#Записываем “Number: строка из файла” из одного файла в другой (print)
#output_file = open('song.txt','r')
#with open ('number_file','w') as file_num
#   j = 1
#   for i in output_file:
#       print(str(j) + ":" + i, file = file_num)
#       j+=1

#Записывает в новый файл все слова в алфавитном порядке из другого файла с
#текстом. Каждое слово на новой строке.
#* (доп.) Рядом со словом укажите сколько раз
output_file = open('october.txt','r')
#with open ('abc_file','w') as file_abc:
for i in output_file:
    print(i)
output_file.close()

