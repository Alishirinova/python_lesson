# работа с файлами
import os

current_dir = os.getcwd()
print(current_dir)

list_dir = os.listdir()# даст содержимое текущего каталога, если () пустые
print(list_dir)

list_dir = os.listdir('..')# две точки поднимают к верхней папке, не рекомендуется юзать
print(list_dir)

#создаем путь через джоин
tmp_path = os.path.join('python_lesson','lesson_5_1.py')
print(tmp_path)


def get_files_from_dir(base_dir, full_path=True):
    # base_dir = "test"
    list_dir = os.listdir(base_dir)
    print(list_dir)
    files = []
    for file_object in list_dir:
        path_object = os.path.join(base_dir, file_object)
        if os.path.isfile(path_object):
            files.append(path_object if full_path else file_object)
    return files

alphabet_files = get_files_from_dir('alphabet')
print(alphabet_files)
test_files = get_files_from_dir('test')
print(test_files)

#создание папки:
# def create_dir(path):
#     try:
#         os.mkdir(path)
#     except FileExistsError:
#         pass
# create_dir("test_dir_2")

os.makedirs('test_3_dir/test_4_dir', exist_ok=True)
