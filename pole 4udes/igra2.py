import random

def viktorina(): #Задаем функцию для викторины
    with open ('voprosi.txt','r',encoding='utf8') as file:
        spisok_voprosov = file.read().splitlines()
        strocka = random.randrange(0, len(spisok_voprosov))
        vopros_otvet = str(spisok_voprosov[strocka])
        for i in range(0, len(vopros_otvet)):
            if vopros_otvet[i]==';':
                vopros = vopros_otvet[0:i]
                otvet = vopros_otvet[i+1:len(vopros_otvet)]
        return otvet, vopros #Функция выдает ответ и вопрос

otvet, vopros = viktorina() #Задаем переменные

print(vopros)
#Печатаем звездочки для скрытого слова:
skritoje_slovo = []
for bukva in range(0,len(otvet)):
    skritoje_slovo.append('*')
print(''.join(skritoje_slovo))

popitki=0
otgadannije_bukvi = '' #Сначала нет отгаданных букв

while  popitki != 3:
    #Пользоатель вводит свою догадку:
    dogadka = input('Введите букву или слово: ').lower()
    if dogadka == otvet:
        print('Молодцы!');print();break
    if dogadka in otvet and dogadka not in otgadannije_bukvi:
        print ('Есть такая буква!')
        otgadannije_bukvi += dogadka
        podbor_bukv = '' #Для вывода отгаданных и скрытых букв
        for bukva_otveta in otvet:
            if bukva_otveta in otgadannije_bukvi:
                podbor_bukv += bukva_otveta
            else:
                podbor_bukv += "*"
        print("Угаданные буквы: ", podbor_bukv)
    elif dogadka in otgadannije_bukvi:
        print ('Вы уже называли эту букву!')
        popitki += 1
    else:
        print('Такой буквы нет или неверное слово!')
        popitki += 1
    if podbor_bukv == otvet:
       print('Вы правильно назвали все буквы!');print();break
       
if popitki == 3:
    print('Вы не угадали слово! Правильный ответ: {}.'.format(otvet))
    print()
       
if popitki == 3 or podbor_bukv == otvet or dogadka == otvet:
    print('Конец игры!')



