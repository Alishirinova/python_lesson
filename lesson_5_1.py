my_str = 'blablacar'
my_symbol = 'bla'

my_symbol_count = my_str.count(my_symbol)
print(my_symbol_count)


##################2
my_str = 'blablacar'
my_symbol = 'bla'

my_symbol_count = my_str.count(my_symbol)
# print(my_symbol_count*my_symbol) так не подходит, если нужно вывести список
for _ in range(my_symbol_count): # _ имя переменной, которую не используют, чтоб сохранить формулу
    print( my_symbol) #pass если не нужно выполниять принт, но нужно сохранить алгоритм формулы
    res_msg = f'{my_symbol}\n'*my_symbol_count #\n - делает отступ
    print(res_msg.strip()) # стрип - избавляет от лишней табуляции

##################3
my_str = "bla BLA car"
print(len(my_str))
my_str = my_str.lower()
symbols_heap = []

for symbol in my_str:
    if symbol not in symbols_heap:
        symbols_heap.append(symbol)
res_len = len(symbols_heap)
print(res_len) #задача была вывести кол-во символов в тексте

##################3
my_str = 'qwerty'
my_list = []
for index in range (len(my_str)):
    if not index % 2:
        symbol = my_str[index]
        my_list.append(symbol)
# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol) альтернативное решение с помощью enumerate
print(my_list) #задача была заполнить список символами которые стоят на четных местах

##################4
my_str='qwerty'
my_list=[]
str_index = [3, 2, 5, 1, 0, 5]
for index in str_index:
    symbol = my_str[index]
    my_list.append(symbol)
print(my_list)#заполнили список символами из переменной, которые стоят на местах с задаными индексами

##################5
my_number = 2315132131531351315351
digit_count = len(str(my_number))
print(digit_count) # подсчитали кол-во символов в переменной

##################6
# в пайтоне существует алфавит символов, втч цифр. ASCii
#ord("@")  - узнать какой номер у символа
#chr(100)  - проверить, какой символ стоит под этим номером

number_str = str (my_number)
max_symbol = max(number_str) #не работает для разных типов данных
print(max_symbol) #нашли наибольшее число в переменной

##################7
#как работать с сортировкой
my_list = [1,2,3,-8,4]
my_str ='qwerty'
sorted_list = sorted(my_list,reverse=True) #reverse= определяет убывание
print(sorted_list)
sorted_str = sorted(my_str)
print(sorted_str)
# НУЛИ в переменной МОЖНО ОТСЛЕДИТЬ С ПОМОШЬЮ реверса

