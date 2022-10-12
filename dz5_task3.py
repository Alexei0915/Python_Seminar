
print("Крестики-нолики на 2 х")
table = list(range(1,10))
def table_draw(table):
    print("-" * 13)
    for i in range(3):
     print("|",table[0 + i * 3],"|",table[1 + i * 3],"|",table[2 + i * 3],"|")
     print("-" * 13)
def take_input(player_symbol):
    valid = False
    while not valid:
        player_choice = input (F"куда поставим " +  player_symbol+" ?")
        try:
            player_choice= int(player_choice)
        except:
            print("Неверный ввод")
            continue
        if player_choice>=1 and player_choice <=9:
            if(str(table[player_choice-1])not in "XO"):
                table[player_choice-1]= player_symbol
                valid=True
            else:
                print("Тут уже занято")
        else:
            print("Введите от 1 до 9!")

def win(table):
    win_chek = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for any in win_chek:
        if table[any[0]]== table[any[1]] == table[any[2]]:
            return table[any[0]]
    return False
def main(table):
    counter =0
    winner= False
    while not winner:
        table_draw(table)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter >4:
            tmp = win(table)
            if tmp:
                print(tmp,"WINNER!!!!")
                winner = True
                break
        if counter==9:
            print("DRAW!")
            break
        table_draw(table)
main(table)

input("Press Enter for Exit")


