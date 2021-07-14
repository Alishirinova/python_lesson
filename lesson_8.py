#методы словарей
symbols = [ord(symbol) for symbol in 'eyuioa']  # тут список
print(symbols)

symbols = {ord(symbol): symbol for symbol in 'eyuioa'}  # тут словарь
print(symbols)

persons = {'John': 12, 'Jake': 24, 'Anna': 24}
print(persons['Anna'])
persons['Jackob'] = 59  # дополнить словарь
persons['John'] = 73  # дополнить, изменить словарь
persons['John'] = print()  # круглые скобки после принт приводят к значению None
print(persons)

# print(persons["Vova"]) # вызов по ключу которого нет приведет к ошибке
print(persons.get("Vova", 100))  # возвращает заданое условие при ошибке

result = "Anna" in persons  # in проверяет только ключи
print(result)

if "Vova" not in persons:
    persons['Vova'] = 41
print(persons)

key = 'Anna'
# if key not in persons:
#     persons[key] = 41
# print(persons)
#

for key in persons:
    print(key, persons[key])

for key, value in persons.items():
    print(key, value) #альтернатива, удобнее, если работа идет с многобуквенными названием таблицы

print(type(persons.keys()),persons.keys())
print(type(persons.values()),persons.values())

value = persons.pop('Jackob')
print('>>>>>>',value) #можно подхватить значение, которое мы удаляем
print(persons)



