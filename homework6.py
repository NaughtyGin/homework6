my_dict = {'Semen' : 1980, 'Misha' : 1990, 'Gosha' : 1970}
print('Словарь:', my_dict)
print('Одно значение по ключу:', my_dict['Misha'])
my_dict['Roman'] = 1975
print('Значение по добавленному ключу:', my_dict['Roman'])
print('Значение по отсутствующему ключу:', my_dict.get('Serg'))
my_dict.update({'Polina' : 1993, 'Elena' : 1999})
print('Обновленный слварь:', my_dict)
a = my_dict.pop('Misha')
print('Значение из пары, удалённой по ключу:', a)
print('Итоговый словарь:', my_dict)
print(' ') # для отделения на консоли частей по словарям и по множествам
my_set = {1, 2, 3, 2, 1, 1, True, 'Urban', (1, 2, 3, 4, 5), True}
print('Множество:', my_set) # улевы значения не печатаются (но и не ругается) - в лекции аналогично!
my_set.add('University')
my_set.add(6.1)
print('Добавлены 2 элемента:', my_set)
print('Удален один элемент:', my_set.remove(6.1))
print('Итоговое множество:', my_set)