#создаем список:
new_list=[]
new_list.append('first')
new_list.append('second')
new_list.append([1,2,3])
last_value=new_list.pop() #удаляет последний элемент, но сохраняет отдельно
print(new_list)
print(last_value)