"""
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
Sample Input:

attraction
buzzzz
Sample Output:

atraction
buz
"""
from sys import stdin
import re

for word in stdin:
    lst_in = word
    match = re.finditer(r'(\w)\1+', lst_in)
    for item in match:
        lst_in = lst_in.replace(item[0], item[0][0])
    print(lst_in, end='')
