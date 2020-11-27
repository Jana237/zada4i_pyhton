import random
def get_quest():
    #open file with questions
   vopros = open("game.txt","r",encoding=("utf-8"))
   #read question list
   question_list = vopros.read().splitlines()
   #choose a random question
   questnum = random.randrange (0,len(question_list))
   questline = str (question_list[questnum])
   #searching for ";" in line
   for i in range(0,len(questline)):
       if questline[i]==";":
           vopros = questline[0:i]
           otvet = questline[i+1:len(questline)]
           return otvet, vopros
counter=0
while True:
    initCheck="exit"
    print("Начать игру нажав любую кнопку! Нажмите '",initCheck,"' если хотите выйти из игры.")  
    init=input()
    if init==initCheck:
        print("ТЫ ответил ",counter," вопрос!")
        break
    otvet, vopros = get_quest()
    print(vopros)
    print(otvet)
    #hiding the answer, but not the whitespace
    view=[]
    check=""
    for i in range (0,len(otvet)):
        if otvet[i]==" ":
            view.append(" ")
        else:
            view.append("*")
    print("".join(view))
    #giving a 3 tries to guess a character or answer
    k=3
    while k>0:
        ans = input('Введите букву или слово:')
        if ans.lower() == otvet.lower():
            counter=counter+1
            print("Молодцы!. Правильный ответ {otvet}");
            break
        elif (ans.lower() in otvet.lower()):
            print("Есть такая буква!")
            for i in range(0,len(otvet)):
                if otvet[i].lower()==ans.lower():
                    if otvet[i].isupper():
                        view[i]=ans.upper()
                        check="".join(view)
                    else:
                        view[i]=ans.lower()
                        check="".join(view)
        else:
            print("Такой буквы нет или неверное слово! Осталось ",k-1," попытки(а).")
            k=k-1
        if check.lower()==otvet.lower():
            counter=counter+1
            print(f"Вы правильно назвали все буквы! Загаданное слово {otvet}");break
        print(check)
       # print(answer)
        if k==0:
            print(f"Конец игры! Вы неправильно ответили на вопрос. Загаданное слово было {otvet}")
            print()
            counter=0
            

