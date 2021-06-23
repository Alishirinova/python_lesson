
test_str = "qwertydjkfhawi7465$#&^&%"
print(test_str)
result = []
for symbol in test_str:
    if symbol.lower() not in "eyuioa" and symbol.isalpha():
    #    print (f"symbol: {symbol}")
        result.append(symbol)
        print(result)
    join_str ="_".join(result)
    print(join_str)

# #tuple - кортеж, неизменяемый тип
# #list - список, изменяемый тип
# my_tuple = (1,2,"qwe", (-1,0),None)
# print(type(my_tuple),my_tuple)

# my_list = [1,2,"qwe", (-1,0),None]#[1,2,3,3.0]
# print(type(my_list),my_list)
# # index=-1 #тут задаем
# # #my_tuple=my_tuple[::-1]
# # my_list[index] = 3
# # value_tuple = my_tuple[index]
# # value_list = my_list[index]
# # print(value_tuple,value_list)

#СРЕЗЫ как в строках

# #приведение к типам
# new_list=list(my_tuple)
# new_tuple=tuple(my_list)
# print(type(new_tuple),new_tuple)
# print(type(new_list),new_list)#можем поменять кортеж и лист



