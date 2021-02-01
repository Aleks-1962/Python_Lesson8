"""Собственный  класс-исключение, обрабатывающий ситуацию деления на нуль """


class BadDenominator(Exception):
    def __init__(self, text):
        self.text = text


def valid_denom():
    try:
        v_numer, v_denom = map(int, input('Введите числитель и знаменатель, через пробел - ').split())
        print(v_numer, v_denom)
        if v_denom == 0:
            raise BadDenominator('Был введен 0 в качестве знаменателя. Делить на нельзя!')
        else:
            return f'Результат = {v_numer / v_denom}'
    except ValueError:
        return f'Не правильный тип переменной\nБыли введены не числовые значения'
    except BadDenominator as err_zero:
        return err_zero
#    except KeyboardInterrupt:
#        return ('Работа программы принудительно прервана')
#        exit()
    finally:
        print('Работа программы завершена')


print(valid_denom())
