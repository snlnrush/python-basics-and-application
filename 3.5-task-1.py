"""
Вам дана частичная выборка из датасета зафиксированных преступлений,
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""
fin = open('Crimes.csv', 'r', encoding='utf-8')

dict_crime = {}
lst_crime = []

for line in fin.readlines():
    date = line.split(',')[2]
    crime = line.split(',')[5]
    year = date.split(' ')[0][-4:]
    if year == '2015':
        dict_crime[crime] = dict_crime.get(crime, 0) + 1

for key, val in dict_crime.items():
    lst_crime.append((val, key))

lst_crime.sort(reverse=True)

print(lst_crime[0][1])

fin.close()
