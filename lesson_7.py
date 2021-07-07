my_str = 'My name is Vova. I m 41. JHYGhg'
result = []
for symbol in my_str:
    if symbol.isupper():
        result.append(symbol)
# result = [symbol for symbol in my_str if symbol.isupper()]
str_1 = ''.join(result)
print(str_1) #задача выбрать все большые бувкы и выбрать их в строку

result = []
for symbol in my_str:
    if symbol.islower(): #if not symbol.isupper()
        result.append(symbol)
# result = [symbol for symbol in my_str if symbol.isupper()]
str_2 = ''.join(result)
print(str_2)#задача выбрать все маленькие бувкы и выбрать их в строку

str_3=''
for symbol in my_str:
    if symbol.islower() and symbol not in 'eyuioa':
        result.append(symbol)
        # result = [symbol for symbol in my_str if symbol.isupper()]
str_3 = ''.join(result)
print(str_3)  # задача выбрать все маленькие согласные бувкы и выбрать их в строку

str_4 = ''
for symbol in my_str:
    if symbol.islower():
        str_4 += symbol.upper()
    elif symbol.isupper():
        str_4 += symbol.lower()
    else:
        str_4 += symbol
        # result = [symbol for symbol in my_str if symbol.isupper()]
print(str_4)  # поменять большые на маленькие и наоборт

big_letters =[]
little_a_letter =[]
little_b_letter = []
symbols = []

for symbol in my_str:
    if symbol.isupper():
        big_letters.append(symbol)
    elif symbol.islower() and symbol in 'eyuioa':
        little_a_letter.append(symbol)
    elif symbol.islower() and symbol  not in 'eyuioa':
        little_b_letter.append(symbol)
    else:
        symbols.append(symbol)
result = sorted(big_letters)+sorted(little_a_letter)+sorted(little_b_letter)+symbols
res_str = ''.join(result)
print(res_str)#задача - отобрать большие, маленькие гласные, малеьнькая согл с сортировкой в алфавит порядке

