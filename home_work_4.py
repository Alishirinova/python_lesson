my_list = [500, 1, 2, 3, 50, 120, 150, 1100]
for n in my_list:
    if n > 100:
        print(n)
    else:
        None

###################################################2)
my_list = [500, 1, 2, 3, 50, 120, 150, 1100]
my_result = []
for n in my_list:
    if n > 100:
        my_result.append(n)
print(list(my_result))

###################################################3)
my_list = [1, 2, 3, 4, 5]  # , 2, 3, 4, 5
number = 0 if len(my_list) < 2 else (my_list[-1] + my_list[-2])
my_list.append(number)
print(my_list)

###################################################4)

value = input('введите любое число: ')
try:
    value = float(value)
    result = value**-1
except ValueError:
    print('это не то что надо')
except ZeroDivisionError:
    print('введи не ноль')
print(result)

###################################################5)
my_str = '0123456789'
result =[]

for symb_1 in my_str:
    for symb_2 in my_str:
        result.append(int(symb_1+symb_2))
print(result)













