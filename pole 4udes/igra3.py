schotchik_voprosov=0 
while schotchik_voprosov<10:
    def viktorina(): 
        with open ('voprosi.txt','r',encoding='utf8') as file:
            spisok_voprosov = file.read().splitlines()
            global schotchik_voprosov
            strochka = spisok_voprosov[schotchik_voprosov]
            vopros_otvet = str(strochka)
            for i in range(0, len(vopros_otvet)):
                if vopros_otvet[i]==';':
                    vopros = vopros_otvet[0:i]
                    otvet = vopros_otvet[i+1:len(vopros_otvet)]
            return otvet, vopros 
    otvet, vopros = viktorina() 
    print(vopros)
    skritoje_slovo = []
    for bukva in range(0,len(otvet)):
        skritoje_slovo.append('*')
    print(''.join(skritoje_slovo))
    popitki=0
    otgadannije_bukvi = ''
    while  popitki != 3:     
        dogadka = input('Введите букву или слово: ').lower()
        if dogadka == otvet:
            print('Молодцы!');print();break
        if dogadka in otvet and dogadka not in otgadannije_bukvi:
            print ('Есть такая буква!')
            otgadannije_bukvi += dogadka
            podbor_bukv = '' 
            for bukva_otveta in otvet:
                if bukva_otveta in otgadannije_bukvi:
                    podbor_bukv += bukva_otveta
                else:
                    podbor_bukv += "*"
            print("Угаданные буквы: ", podbor_bukv)
        elif dogadka in otgadannije_bukvi:
            print ('Вы уже называли эту букву!','осталось',3-popitki,'попытки(а)')
            popitki += 1
        else:
            print('Такой буквы нет или неверное слово!','осталось',3-popitki,'попытки(а)')
            popitki += 1
        if podbor_bukv == otvet:
            print('Вы правильно назвали все буквы!');print();break     
    if popitki == 3:
        print('Вы не угадали слово! Правильный ответ: {}.'.format(otvet))
        print()       
    schotchik_voprosov+=1           
if schotchik_voprosov==10:
        print('Конец игры!')
