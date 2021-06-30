




#создание списка из двух

my_list_1 = [1, 2, 3, 4,6,5,7]
my_list_2 = [10, 20, 30, 40, 50]
# ctr+alt+l - автоформатирование
my_result=[]
min_len_lists = min(len(my_list_1),len(my_list_2))
for index in range (min_len_lists):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])

last_values_list_1 = my_list_1[min_len_lists:]
last_values_list_2 = my_list_2[min_len_lists:]
my_result=my_result+last_values_list_2+last_values_list_1
print(my_result)

#########
#id - номер объекта в памяти, помагает при проверке источника для записи данных

my_list = [1, 2, 3]
print(id(my_list))
my_list = [1, 2, 3, 4, 5]
print(id(my_list))
my_list.append(6)
print(id(my_list))
########
my_list = [1, 2, 3]
result = []
print(id(result))

result = my_list + result
print(id(result))
result += my_list #для чисел как сумма, для списка по другому
print(id(result))


######### генератор списков - короткая запись цикла for
