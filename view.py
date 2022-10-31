def show_menu():
    print('1. Вывести весь список')
    print('2. Добавить запись')
    print('3. Удалить запись')
    print('4. Изменить номер телефона')
    print('5. Перенести данный из справочника 1 в справочник 2')
    return int(input('Выберете действие '))

def show_data(res):
    for i,row in enumerate(res):
        if i==0:
            print(f'n/n {", ".join(row)}')
        else:
            print(i, ' '.join(row)) 

def add_info():
    print('Введите Фамилию Имя и телефон через пробел')
    info=input().split()
    return info

def del_note():
    print('Введите номер строки для удаления ')  
    return int(input())

def change_tel():
    print('Введите номер строки для изменения')
    print('Введите новый номер телефона')
    return int(input()),input()