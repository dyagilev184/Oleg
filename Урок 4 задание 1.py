""" 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы
сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами."""

import sys
f_obj, name_v, rate_v, hours_v = sys.argv
print(f_obj)
def calculatet_v (rate, hours):
    try:
        print(f'Сотрудник {name_v} заработал {int(rate) * int (hours) * 1.30 }')
    except TypeError:
        print("Несоответствующий тип")
        exit()

calculatet_v(rate_v, hours_v)


