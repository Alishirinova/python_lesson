# менеджер контекста r - чтение, w - запись
with open('lesson10.py', 'r') as py_file:
    data = py_file.readlines()  # readlines - выводить все в строку
print(data, type(data))
data.append("#FINISH")
with open('lesson10_new.py', 'w') as py_file:
    py_file.writelines(data)

# создание функий для заданых целей:
import os
import string


def create_dir(path):
    os.makedirs(path, exist_ok=True)


create_dir('alphabet')


def create_file(path,symbol):
    filename = f'{path}/{symbol}.txt'
    with open(filename,'w') as txt_file:
        txt_file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))


def create_file_in_dir(path):
    for letter in string.ascii_lowercase:
        create_file(path,letter)

def get_tanos_click(path):
    files = os.listdir(path)
    files = list(set(files))[:len(files)//2]
    for file in files:
        os.remove(os.path.join(path,file))
    print(files)

create_file_in_dir('alphabet')

get_tanos_click('alphabet')


