from constants import ROD_PRICE


def save_money():
    with open('money.txt', '+w', encoding='utf-8') as f:
        f.writelines(str(MONEY))


def get_money():
    with open('money.txt', 'r', encoding='utf-8') as f:
        money = f.readline()
        return int(money)


def save_rod():
    with open('rods.txt', '+w', encoding='utf-8') as f:
        for e in bought_rods:
            f.writelines(str(e) + '\n')


def get_rods():
    with open('rods.txt', 'r', encoding='utf-8') as f:
        tmp = list()
        for rods in f.readlines():
            tmp.append(int(rods))
        return tmp


def save_progress():
    save_rod()
    save_money()


MONEY = get_money()
bought_rods = get_rods()
CURRENT_MONEY = 0
cur_rod = 0
rod1_text = f'Выбрано' + f'{ROD_PRICE[0]}$' * 0
rod2_text = f'{ROD_PRICE[1]}$'
rod3_text = f'{ROD_PRICE[2]}$'
