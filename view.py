def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('Введите номер опции,которой хотите воспользоваться')
    print('1. Показать весь справочник')
    print('2. Найти номер телефона по имени или фамилии')
    print('3. Найти пользователя по номеру телефона')
    print('4. Добавить нового пользователя в справочник')
    print('5. Выход из справочника')
    number_menu = int(input('пункт меню = '))
    while(number_menu > 5 or number_menu < 1):
        print('введите корректное значение функции меню')
        number_menu = int(input('N = '))
    return number_menu

def output(data):
   return print(data)

output('Упс')