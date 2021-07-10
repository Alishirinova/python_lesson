# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

my_list = [12, 123, 1234, 12345, 123456, 1234567]
new_list = []
for index in range(len(my_list)):
    if not index % 2:
        symbol = my_list[index]
        symbol = str(symbol)[::-1]
        symbol = int(symbol)
        new_list.append(symbol)
    elif index % 2:
        symbol = my_list[index]
        new_list.append(symbol)
print(new_list)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_list = ['a12', '123', '1234', '12345', '123456', 'a1234567']
new_list = []
for index in my_list:
    if index[0] == 'a':
        new_list.append(index)
print(new_list)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_list = ['a12', '12a3', '1234', '12345a', '123456', 'a1234567']
new_list = []
for index in my_list:
    if 'a' in index:
        new_list.append(index)
print(new_list)

# 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.
my_list = [1, 2, 3, "11", "22", 33]
new_list = []
for index in my_list:
    if isinstance(index, str):
        new_list.append(index)
print(new_list)

# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.
my_str = 'qqqqqqqwertttttty'
my_list = []
for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
print(my_list)

# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 ='hello world!'
my_str_2 = 'hello friend!'
my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)
intersection = my_set_1.intersection(my_set_2)
intersection = list(intersection)
print(intersection)

# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу
my_str_1 = 'hello world !'
my_str_2 = 'hello friend !'
my_list_1 = []
my_list_2 = []
for symbol in set(my_str_1):
    if my_str_1.count(symbol) == 1:
        my_list_1.append(symbol)
for symbol in set(my_str_2):
    if my_str_2.count(symbol) == 1:
        my_list_2.append(symbol)
my_set_1 = set(my_list_1)
my_set_2 = set(my_list_2)
intersection = my_set_1.intersection(my_set_2)
intersection = list(intersection)
print(intersection)

# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

person_dict = {'Фамилия': "Иванов",
               'Имя': "Петр",
               'Возраст': "22",
               'Страна': 'Уругвай',
               'Проживание': {'Город': 'Монтовидео', 'Улица': 'Bulevar Aparicio Saravia,5'},
               'Работа': {'Наличие': 'имеется', 'Должность': 'Продавец АТБ'}
               }

print(person_dict['Фамилия'])

# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло

cake_recipe = {'Коржи': {'Мука': '500 г', 'Молоко': '0,5л', 'Масло': '3 ст.л', 'Яйцо': '2 шт'},
               'Крем': {'Сахар': '10ст. л.', 'Масло': '100 г', 'Ваниль': 'по желанию', 'Сметана': '200 гр'},
               'Глазурь': {'Какао': '200 г', 'Сахар': '10ст. л.', 'Масло': '2 ст.ложки'}

}
print(cake_recipe['Глазурь'])
