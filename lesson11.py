#json csv
# импорт из файла
import json


def wtite_json(filename, data):
    data = [1, 2, 3, 4, 5]
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)


def read_json(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)
    return data


data_list = [1, 2, 3, 4, 5]
data_dict = {'name': 'Jhon',
             'age': '13',
             'job': {'title': "Data Ingenier",
                     'price': '100$'}}

filename = 'data_list.json'
wtite_json(filename, data_dict)
data = read_json(filename)

