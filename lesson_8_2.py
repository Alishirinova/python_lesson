persons = {'John': 12, 'Jake': 24}
persons_other = {'Jake': 64, 'Anna': 24}

persons.update(persons_other) #функция уничтожает старый результат, нужно быть осторожным при работе

print(persons)
# лучше создать новый словарь и его дважды апдейтнуть
persons_result = {}
persons_result.update(persons)
persons_result.update(persons_other)
print(persons_result)
persons_result = {**persons, **persons_other}  # магия апдейта словаря с **
print(persons_result)


