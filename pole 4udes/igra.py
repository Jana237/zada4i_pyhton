import random
def get_vopros():
    # Открыть файл с вопросами
   vopros = open("game.txt","r",encoding=("utf-8"))
   
   vopros_list = vopros.read().splitlines()
   # Выберите случайный вопрос
   voprosnum = random.randrange (0,len(vopros_list))
   voprosline = str (vopros_list[voprosnum])
   
   for i in range(0,len(voprosline)):
       if voprosline[i]==";":
           vopros = voprosline[0:i]
           otvet = voprosline[i+1:len(voprosline)]
           return otvet, vopros
popitki=0
while True:
    initCheck="exit"
    print("Начать игру нажав любую кнопку! Введите '",initCheck,"' если хотите выйти из игры.")  
    init=input()
    if init==initCheck:
        print("ТЫ ответил ",popitki," вопрос!")
        break
    otvet, vopros = get_vopros()
    print(vopros)
    # Скрыть ответ
    skritoje_slovo=[]
    for bukva in range (0,len(otvet)):
        skritoje_slovo.append("*")
    print(" ".join(skritoje_slovo))
    popitki = 0
    otgadannije_bukvi=""
    
    # Три попытки. Угадай букву или слово.
    k=3
    while k>0:
        ans = input('Введите букву или слово:')
        if ans.lower() == otvet.lower():
            popitki=popitki+1
            print("Молодцы!. Правильный ответ!");print()
            break
        elif (ans.lower() in otvet.lower()):
            print("Есть такая буква!")
            for i in range(0,len(otvet)):
                if otvet[i].lower()==ans.lower():
                    if otvet[i].isupper():
                        skritoje_slovo[i]=ans.upper()
                        check="".join(skritoje_slovo)
                    else:
                        skritoje_slovo[i]=ans.lower()
                        check="".join(skritoje_slovo)
        else:
            print("Такой буквы нет или неверное слово! Осталось ",k-1," попытки(а).")
            k=k-1
        if check.lower()==otvet.lower():
            popitki=popitki+1
            print(f"Вы правильно назвали все буквы! Загаданное слово {otvet}");break
        print(check)
       
        if k==0:
            print(f"Конец игры! Вы неправильно ответили на вопрос. Загаданное слово было {otvet}")
            print()
            popitki=0
