my_str = 'blablacar'
my_symbol = 'bla'

my_symbol_count = my_str.count(my_symbol)
print(my_symbol_count)


##################2
my_str = 'blablacar'
my_symbol = 'bla'

my_symbol_count = my_str.count(my_symbol)
# print(my_symbol_count*my_symbol) так не подходит, если нужно вывести список
for _ in range(my_symbol_count): # _ имя переменной, которую не используют, чтоб сохранить формулу
    print( my_symbol) #pass если не нужно выполниять принт, но нужно сохранить алгоритм формулы
    res_msg = f'{my_symbol}\n'*my_symbol_count #\n - делает отступ
    print(res_msg.strip()) # стрип - избавляет от лишней табуляции

##################3
my_str = 'bla BLA car'
my_str = my_str.lower()
symbols_heap = []
for symbol in my_str:
    if symbol not in symbols_heap:
        symbols_heap.append(symbol)
    res_len = len(symbols_heap)
    print(res_len) ## тут чет не то, нужно посмотреть видео и доработать


