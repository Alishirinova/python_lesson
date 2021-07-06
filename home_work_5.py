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
