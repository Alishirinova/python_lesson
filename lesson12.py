# функции сортировки

# my_list = [12, 3, 45, 23, -10, 1]
# sorted_list = sorted(my_list, reverse=True, key=abs)
# print(sorted_list)
#

# def sort_by_len_and_name(name):
#     return len(name), name  # сортировка и по длине и по алфавиту
#
# my_str_list = ['Jhon', 'Jack', 'Jacob', 'Max', 'Violeta']
# sorted_my_str_list = sorted(my_str_list)  # по алфавиту
# print(sorted_my_str_list)
#
# sort_str_list = sorted(my_str_list, key=len)  # по длине
# print(sort_str_list)
#
# sort_str_list = sorted(my_str_list, key=sort_by_len_and_name)  # по длине
# print(sort_str_list)


# def sort_by_price(price_dict):  # функуия сортировки по прайсу
#     price = price_dict['price']
#     name = price_dict['product']
#     return price, name  # функция может отрабатывать по нескольким  условиям
#
#
# price_list = [{'product': 'milk', 'price': 23},
#               {'product': 'ice-cream', 'price': 18},
#               {'product': 'meat', 'price': 120},
#               {'product': 'pepsi-cola', 'price': 10},
#               {'product': 'papsi-cola', 'price': 10},
#               {'product': 'paasi-cola', 'price': 10},
#               {'product': 'coca-cola', 'price': 10},
#               ]
# sorted_price_list = sorted(price_list,key=sort_by_price)
#
# print(sorted_price_list)

# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ
import re

my_string = 'sjhfLKWHD;Oi1354654531321351jxLKAKSMxklasM,210.0.7.0asjdhf;skjah sdjfksgfkj 200.3.11.200:5400 askjhflkjh'
# tempfile = r'\d+'  # \d - любая цифра
tempfile = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'  # поможет споймать компинацию с точкой - в нашем случае айпи адрес
result = re.findall(tempfile, my_string)
print(result)
