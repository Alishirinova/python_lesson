value=input('введи целое число ')
# if value.isdigit():
#     value=int(value)
#     result=value*2
#     print(result)
# else:
#     print('вы ввели не число')

try:
    value=float(value)
    result=1/value
    print(result)
except (ZeroDivisionError,ValueError):   # ValueError: это комапнда для проверки ошибки
    print('что-то пошло не так, попробуй еще')
    result=0
    print(result)