#множество set, уникальные элементы
my_list = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 2]
my_set=set(my_list)
print(my_set)
# my_list_unique = list(set(my_list)) - убивает дубли , сет не сохраняет порядок
my_list_unique = list(my_set)
print(my_list_unique)
new_set = {1,2,54,53,54,54}
print(new_set)
new_set=list(new_set)
print(new_set)

#см лессон 5, номр 3 сколько разных символов встречается в строке:
my_str = 'qqqqqqqwwwwwwwwweeeeeeeeeerrrrrrrtttttty'
res_len =len(set(my_str))
print(res_len)
# как подсчитать кол-во записей каждого символа
for symbol in set(my_str):
    print(symbol, my_str.count(symbol))

######работа с множествами ( инер джоин, лефт и тд)
my_str_1 ='qwerty'
my_str_2 = 'qweasd'
my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)
intersection = my_set_1.intersection(my_set_2) #общие элементы
print(intersection)
union = my_set_1.union(my_set_2) #все элементы двух множест
print(union)
difference =my_set_1.difference(my_set_2) #уникальные, неповторяющиеся элементы из my_set_1
print(difference)
difference_2 = my_set_2.difference(my_set_1) #уникальные, неповторяющиеся элементы из my_set_2
print(difference_2)

########словарь: dict -не гарантирует порядок, все ключи уникальны, остается последняя запись/значение
# ключи - любые неизменяемы обьекты (строка, картеж, число)
#значения - любые объекты

# triangle = [[1,1,],[2,3],[4,-2]]
# print(triangle[1][1])
test_dict = {11:'qwerty',
             '11':12,
             (1,2,'qwe'):'test'}
print(type(test_dict))
print(test_dict)

triangle = {'A': {'x': 1, 'y': 1},
            'B': {'x': 2, 'y': 3},
            'C': {'x': 4, 'y': -2}}
print(triangle['B']['y'])
print(triangle)
