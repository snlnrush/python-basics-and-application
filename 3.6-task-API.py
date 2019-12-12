"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать,
существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring

У вас есть неограниченное число попыток.
Время одной попытки: 5 mins
"""
from urllib.request import urlopen
import json

f_in = open('dataset_24476_3.txt', 'r', encoding='utf8')
lst_numbers = f_in.readlines()
f_in.close()

for number in lst_numbers:
    url = 'http://numbersapi.com/{}/math?json=true'.format(number.strip())
    resp = urlopen(url)
    resp_tmp = resp.read().decode('utf8')
    dict_resp = json.loads(resp_tmp)
    if dict_resp['found'] is True:
        print('Interesting')
    else:
        print('Boring')
