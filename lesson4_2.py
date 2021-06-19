#ИТЕРАЦИЯ
# count = 10
# while count >0: #вайл=бесконечный цикл
#     #count +=1 #увеличение на 1
#     count -= 1  # уменьшение на 1
#     print(f"count={count}")
#
tmp_value=5

go_game=True

while go_game:
    value=input('введи число от 1 до 10: ')
    if str(tmp_value)==value:
        go_game=False
        print('ура, угадал!')

##ДЗ* давать подсказки типа "побробуй больше / меньше"