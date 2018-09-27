text = "We are not what we should be!"\
       "We are not what we need to be."\
       "But at least we are not what we used to be."
#Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
text = text.replace("!"," ")
text  = text.replace("."," ")
text = text.strip()
text = text.upper()
l = text.split(" ")
print(len(l))

#Удалите знаки препинания (пройдитесь циклом все слова и удалите
#методом strip знаки препинания)

# Выведите слова в алфавитном порядке (найдите метод списка, который
#сортирует)
l = sorted(l)
print(l)

#Усложнённое ** (можно сначала его не делать):

# Посчитать, сколько раз встречается каждое слово.
#(Подсказка: создавать словарь, где ключи — это слова из текста, а в значениях
#подсчитываем количество «встречаний» этого слова)

dct={}
for i in l:
        if i in dct:
            dct[i] += 1
        else:
            dct[i] = 1
for key,value in dct.items():
    print(key,value,end='\n')
