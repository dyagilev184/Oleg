""" 6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count()
 и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие
  его завершения. #### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10
— завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import  count, cycle

list_int = []

a = int (input(" Укажите первое число"))
n = int (input(" Укажите последне число"))

for x in count (a):
    if x > n:
        break
        print(x)
        list_int.append(x)

print()
print(list_int)

count = 0
for item in cycle(list_int):
    if count >= len(list_int):
        break
        print(item)
        count += 1