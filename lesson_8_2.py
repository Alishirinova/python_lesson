persons = {'John': 12, 'Jake': 124}
persons_other = {'Jake': 64, 'Anna': 24}

# persons.update(persons_other) #функция уничтожает старый результат, нужно быть осторожным при работе

print(persons)
# лучше создать новый словарь и его дважды апдейтнуть
persons_result = {}
persons_result.update(persons)
persons_result.update(persons_other)
print(persons_result)
persons_result = {**persons, **persons_other}  # магия апдейта словаря с **
print(persons_result)

max_age = max(persons_result.values())
print(max_age )# плохое решение для определения макс, тк первый словарь ( с возможно большими значениями) перетерт

max_age = max(max(persons.values()), max(persons_other.values()))
print(max_age)

products = [{"name": 'water', 'price': 12, 'title': "bonaqua"},
            {"name": 'bread', 'price': 0.3, 'title': "baton"},
            {"name": 'bread', 'price': 5, 'title': "baton"},
            {"name": 'apple', 'price': 25, 'title': "Gloden"}]
for product in products:
    print(product['title'])
    product['sale']= True
print(products)
bread_prices=[]
for product in products:
    if product['name']=='bread':
        print(product['price'])
        bread_prices.append(product['price'])
        print(bread_prices)
        product['price'] *= 2  # увеличили цену в два раза
        print(products)
        product['price'] = product['price'] * 1.1 - 1
        print(products)

#домашка 1- сделать список возростов  и по нему определить имена мин возраста
# 2 - фото доски
