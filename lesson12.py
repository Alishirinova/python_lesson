# функции сортировки

# my_list = [12, 3, 45, 23, -10, 1]
# sorted_list = sorted(my_list, reverse=True, key=abs)
# print(sorted_list)
#
# my_str_list = ['Jhon', 'Jack', 'Jacob', 'Max', 'Violeta']
# sorted_my_str_list = sorted(my_str_list)  # по алфавиту
# print(sorted_my_str_list)
#
# sort_str_list = sorted(my_str_list, key=len)  # по длине
# print(sort_str_list)

price_list = [{'product': 'milk', 'price': 23},
              {'product': 'ice-cream', 'price': 18},
              {'product': 'meat', 'price': 120},
              {'product': 'coca-cola', 'price': 10},
              ]
sorted_price_list = sorted(price_list)
print(sorted_price_list)