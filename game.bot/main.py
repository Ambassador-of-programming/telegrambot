# нужно спросить варианат  
# компютер должкм выбрать варианат 
# вы должны сравнить 
from random import choice

varianat = {
    1: 'камень',
    2: "ножницы",
    3: "бумага"
}

def varianat_game(user_choice: int) -> str:
    coumputer_choice = choice(list(varianat))
    if user_choice == coumputer_choice:
        return 1,f"Ничья, Бот выбрал {varianat[coumputer_choice]}"
    elif user_choice == 1 and coumputer_choice == 2 \
        or user_choice == 2 and coumputer_choice == 3 \
            or user_choice == 3 and coumputer_choice == 1:
        return 2,f"Вы выйграли, Бот выбрал {varianat[coumputer_choice]}"
    
    elif user_choice == 1 and coumputer_choice == 3 \
        or user_choice == 2 and coumputer_choice == 1 \
            or user_choice == 3 and coumputer_choice == 2:
        return 3,f"Вы проиграли, Бот выбрал {varianat[coumputer_choice]}"

    else:
        return 'Выберите корректный ответ'

def sticker(res:int)->str:
    list_win=['sitker/win.tgs']
    list_nich=['sitker/nishiya.tgs']
    list_lose=['sitker/fall.tgs']
    if res==1:
        stk = open(choice(list_nich),'rb')
        return stk
    elif res==2:
        stk = open(choice(list_win),'rb')
        return stk
    if res==3:
        stk = open(choice(list_lose),'rb')
        return stk
# while True:print(variant_game(int(input('>> 1.kamen 2.nojnicy 3.bumaga\n>>> '))))
# while True: print(varianat_game(int(input(">>> 1. kamen 2. nojnitsy 3. bumaga /n>>>"))))