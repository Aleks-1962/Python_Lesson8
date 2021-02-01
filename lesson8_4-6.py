""" Создаем базовые классы, описывающий склад «Склад оргтехники» и класс «Оргтехника»
В базовом классе определить параметры, общие для приведенных типов.
 Создаем классы-наследники. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
 В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
 Создаем методы отвечающие за приём оргтехники на склад и передачу в подразделение компании.
 Для хранения данных о наименовании и количестве единиц оргтехники, используем словарь.
 Создаем механизм валидации вводимых пользователем данных"""


class SkladTech:
    def __init__(self):
       self.dict = {}
    '''Создаем словарь'''

    def add_tech(self, technika):
        self.dict.setdefault(technika.name_t, []).append(technika)
        print(self.dict)
        ''' добавляем в словарь по названию оборудования'''

    def extract_tech(self, name_t):
        if self.dict[name_t]:
            self.dict.setdefault(name_t).pop(0)
            ''' извлекаем по названию оборудования'''
        else:
            return f' На склад нет '


#    def __add__(self, other):
#        rez = self.kol_vo + other.kol_vo
#       return f' На склад поступило - {other.kol_vo_a},
#               на складе всего - {rez}'

#    def __sub__(self, other):
#        rez = self.kol_vo - other.kol_vo
#       return f' С склада выдано - {other.kol_vo}, на складе всего - {rez}'



class Technika:
    def __init__(self, name_t, price_t, kol_vo):
        self.name_t = name_t
        self.price_t = price_t
        self.kol_vo = kol_vo

    def income(self, item):
        while True:
            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ').upper()
            if q == 'Q' or q == 'q':
                print('Выход из режима ввода данных!')
                break
            else:
                try:
                    name_t = input(f'Введите наименование - ')
                    price_t = float(input(f'Введите стоимость товара - '))
                    kol_vo = int(input(f'Введите количество - '))
#                   item = {'Наименование': name_t, 'Стоимость товара': price_t, 'Количество': kol_vo}

                except ValueError:
                    print('Недопустимое значение!')

    def __repr__(self):
        return f'{self.name_t}_{self.price_t}_{self.kol_vo}'
    '''добавляем значения по названию оборудования'''


class Printer(Technika):
    def __init__(self, name_t, price_t, kol_vo):
        super().__init__(name_t, price_t, kol_vo)
        return


class Scaner(Technika):
    def __init__(self, name_t, price_t, kol_vo):
        super().__init__(name_t, price_t, kol_vo)
        return


class Copier(Technika):
    def __init__(self, name_t, price_t, kol_vo):
        super().__init__(name_t, price_t, kol_vo)
        return



print(dict)
sklad = SkladTech()

# создаем объект и добавляем
scaner = Scaner('Brother ADS-3000N', 85.35, 2)
sklad.add_tech(scaner)
print(f'Добавили на склад: {sklad.dict}')
scaner = Scaner('HP ScanJet Pro 4500 FN', 55.81, 1)
sklad.add_tech(scaner)
print(f'Добавили на склад: {sklad.dict}')
scaner = Scaner('Canon CanoScan LiDE 400', 6.49, 10)
sklad.add_tech(scaner)
print(f'Добавили на склад: {sklad.dict}')
printer = Printer('Xerox Phaser 3020BI', 5.56, 1)
sklad.add_tech(printer)
printer = Printer('HP LaserJet Pro M15w', 7.98, 3)
sklad.add_tech(printer)
printer = Printer('Canon i-SENSYS LBP7110Cw', 20.12, 1)
sklad.add_tech(printer)
copier = Copier('CANON imageRUNNER 2204', 46.12, 2)
sklad.add_tech(copier)
copier = Copier('Kyocera TASKalfa 181 1102KJ3NL0', 22.36, 1)
sklad.add_tech(copier)

# выводим склад
print(f'На складе: {sklad.dict}')

# забираем с склада и выводим склад
sklad.extract_tech('HP ScanJet Pro 4500 FN')
print(f'Выдали со склада: {sklad.dict}')
sklad.extract_tech('Xerox Phaser 3020BI')
print(f'Выдали со склада: {sklad.dict}')