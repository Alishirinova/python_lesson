import requests

import random


def get_quote(lang='ru'):
    url = 'http://api.forismatic.com/api/1.0/'
    params = {'method': 'getQuote ',
              'format': 'json',
              'lang': lang,
              'key': random.randint(1, 999999)}
    req_test = requests.get(url, params=params)
    return req_test.json()


def get_quote(raw_quote):
    return raw_quote['quoteText']


def get_author(raw_quote):
    return raw_quote['quoteAuthor']


for reguest_number in range(10):
    # raw_quote = get_raw_quote() тут ошибка списать у учителя
    quote = get_quote(raw_quote)


print(raw_quote)
