"""«Операции с комплексными числами». Создаем класс «Комплексное число»,
реализуем перегрузку методов сложения и умножения комплексных чисел.
Проверяем работу, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверяем корректность полученного результата."""

# контрольные данные
a = str.replace(str.replace(input('Введите 1 комплексное число в формате n + mj - '), ' ', ''), ',', '.')
b = str.replace(str.replace(input('Введите 1 комплексное число в формате n + mj - '), ' ', ''), ',', '.')
a = complex(a)
b = complex(b)
summa = a + b
multiplication = a * b
print(f'Сумма чисел - {a+b}')
print(f'Произведение чисел - {a*b}')


# Перегрузка методов сложения и умножения
class Cmplx:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, obj):
        self.sumax = self.x + obj.x
        self.sumay = self.y + obj.y

    def __mul__(self, obj):
        self.multx = self.x * obj.x - self.y * obj.y
        self.multy = self.y * obj.x + self.x * obj.y


x = float(input('Введите действительную часть 1 комплексного числа - '))
y = float(input('Введите мнимую часть 1 комплексного числа (j) - '))
a = Cmplx(x, y)
x = float(input('Введите действительную часть 2 комплексного числа - '))
y = float(input('Введите мнимую часть 1 комплексного числа (j) - '))
b = Cmplx(x, y)
a + b
a * b
print('Сумма комплексных чисел -  (%.2f+%.2fj)' % (a.sumax, a.sumay))
print('Произведение комплексных чисел - (%.2f+%.2fj)' % (a.multx, a.multy))
