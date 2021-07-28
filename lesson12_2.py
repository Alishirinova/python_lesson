import random
import string


def generate_string(min_limit=20, max_limit=500):
    len_str = random.randint(min_limit, max_limit)
    res_str = ''.join([random.choice(string.ascii_lowercase) for _ in range(len_str)])
    return res_str


def insert_spaces(some_str):
    go_jump = True
    total_index = 0
    some_list = list(some_str)
    while go_jump:
        jump_index = random.randint(1, 10)
        current_index = total_index + jump_index
        if current_index < len(some_list):
            some_list[current_index] = ' '
            total_index += jump_index
        else:
            go_jump=False
    return ''.join(some_list)


def transform_str(some_tsr):
    return some_tsr


def choice_transform(word):
    word = word.capitalize()
    return word


def transform_str_by_words(some_str):
    new_words = []
    words = some_str.split()
    for word in words:
        word = choice_transform(word)
        new_words.append(word)
    return ''.join(new_words)
# тут якась хня, проверить в коде у Владимира
rand_str = generate_string()
tr_str = insert_spaces(rand_str)
print(tr_str)

print(rand_str)
