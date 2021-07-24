import csv


def read_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, dilimetr=';')
        data = []
        for row in reader:
            data.append(row)
    return data

filename = 'data.csv'
new_data = read_from_csv(filename)
print(new_data)