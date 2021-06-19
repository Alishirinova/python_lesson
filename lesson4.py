value=input('введи целое число ')
# if value.isdigit():
#     value=int(value)
#     result=value*2
#     print(result)
# else:
#     print('вы ввели не число')

try:
    value=float(value)
    result=value*2
    print(result)
except:
    print('число не может быть приведено к типу float')
    result=0
    print(result)