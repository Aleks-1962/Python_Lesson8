""" Реализуем класс «Дата», функция-конструктор которая принимает дату в виде строки формата «день-месяц-год».
В классе реализуем 2 метода:
1-й, с декоратором @classmethod, извлекает число, месяц, год
и преобразовываем их тип к типу «Число».
2-й, с декоратором @staticmethod, проводит валидацию числа, месяца и года (например, месяц — от 1 до 12)."""


class MyData:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split('-'):
            my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if month == 2:
            if 1 <= day <= 28:
                if 1900 <= year <= 2100:
                    return f'Все отлично получилось'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный день'
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if 1 <= day <= 31:
                if 1900 <= year <= 2100:
                    return f'Все отлично получилось'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный день'
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if 1 <= day <= 30:
                if 1900 <= year <= 2100:
                    return f'Все отлично получилось'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный день'
        elif month > 12 or month < 1:
            return f'Неправильный месяц'

    def __str__(self):
        return f'Текущая дата {MyData.extract(self.day_month_year)}'


today = MyData('29-01-2021')
print(today)
print(MyData.valid(11, 11, 2121))
print(MyData.valid(11, 13, 2011))
print (MyData.valid (31, 11, 2021))
