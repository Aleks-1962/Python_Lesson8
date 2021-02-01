""" Создаем собственный класс-исключение, который проверяет содержимое списка на наличие только чисел.
 Данные запрашиваем у пользователя и заполняем список.
 Класс-исключение должен контролировать типы данных элементов списка."""


class MyList:
    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения - '))
                self.my_list.append(val)
                print(f'Добавили в список - {self.my_list}')
            except ValueError:
                print(f'Недопустимое значение')
                m_exit = input(f'Для выхода введите Q, продолжения любой символ - ').upper()

                if m_exit == 'Q':
                    return f'Вы вышли'
                    break


try_except = MyList()
print(try_except.my_input())
