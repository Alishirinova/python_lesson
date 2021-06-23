# copy - позводяет сделать список не зависимым от источника
my_list = [1, 2, 3]
new_list = [my_list.copy()] *3
print(new_list)
my_list.append(4)
print(my_list)
print(new_list)

########################
tmp_value=5
go_game=True
text_message = 'введи число от 1 до 10: '
while go_game:
    try:
        value = int(input(text_message))
        if tmp_value > value:
            text_message = 'попробуй больше'
        elif tmp_value <value:
                text_message = 'попробуй меньше'
        else:
            go_game=False
            print('ура, угадал!')
    except ValueError:
        text_message = "введи число от 1 до 10: "