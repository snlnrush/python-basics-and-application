"""
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
Sample Input:

this is a text
"this' !is. ?n1ce,
Sample Output:

htis si a etxt
"htis' !si. ?1nce,
"""
from sys import stdin
import re

for word in stdin:
    word_in = word
    lst_word = list(word_in)
    match = re.finditer(r'\b\w{2}', word_in)

    for item in match:
        lst_word[item.start()] = item[0][1]
        lst_word[item.start() + 1] = item[0][0]

    print(''.join(lst_word), end='')
