import csv

data = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]


def wtite_to_csv(filename, data, delimiter=';'):
    with open(filename, 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        writer.writerows(data)


def read_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        data = []
        for row in reader:
            data.append(row)
            return data


filename = 'data.csv'
data_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [12, 13, 14]]
wtite_to_csv(filename, data_2)

wtite_to_csv(filename,delimiter=';',data=data_2)

new_data = read_from_csv(filename)
new_data.append([100,200,300])
write_to_csv(data=new_data,filename)
print(new_data)