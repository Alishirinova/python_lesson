#1. Дано целое число (int). Определить сколько нулей в этом числе

value = input('введи целое число ')
print(value.count('0'))

# 2. Дано целое число (int).
# Определить сколько нулей в конце этого числа.
# Например для числа 1002000 - три нуля
my_value = '100200000'
my_list = list(my_value)
my_list.reverse()
my_value_new = "".join(my_list)
my_value_new = int(my_value_new)
my_value_new = str(my_value_new)
result = len(my_value) - len(my_value_new)
print(result)

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1, 2, 3, 4, 6, 5, 7]
my_list_2 = [10, 20, 30, 40, 50]
my_result = []
for index in range(len(my_list_1)):
    if not index % 2:
        symbol = my_list_1[index]
        my_result.append(symbol)
for index in range(len(my_list_2)):
    if index % 2:
        symbol = my_list_2[index]
        my_result.append(symbol)
print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list = [1, 2, 3, 4, 6, 5, 7]
new_list = []
index = my_list[0]
new_list = my_list[1:]
new_list.append(index)
print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 2, 3, 4, 5]
last_value = my_list.pop(0)
my_list.append(last_value)
print(my_list)

