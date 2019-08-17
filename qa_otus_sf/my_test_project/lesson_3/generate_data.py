import random
from itertools import islice

fio = []
cities = []
service = ['+', '-']

with open('data__2.csv', 'r', encoding='Windows-1251') as file:
    # начинаем итерацию с 1 строки, а не с нулевой
    lines = islice(file, 1, None)
    for line in lines:
        # разбиваем по запятой
        data_list = line.split(',')
        # фио добавляем в список fio
        fio.append(data_list[0])
        # города в список cities
        cities.append(data_list[1])

# создаем пустые словари с именами мужчин/женщин
names_of_men = {
    'last_name': [],
    'first_name': [],
    'middle_name': []
}
names_of_women = {
    'last_name': [],
    'first_name': [],
    'middle_name': []
}

for name in fio:
    name_list = name.strip().split(' ')
    # проверяем окончание фамилии/имени
    if name_list[0].endswith('а') or name_list[1].endswith('а'):
        names_of_women['last_name'].append(name_list[0])
        names_of_women['first_name'].append(name_list[1])
        names_of_women['middle_name'].append(name_list[2])
    else:
        names_of_men['last_name'].append(name_list[0])
        names_of_men['first_name'].append(name_list[1])
        names_of_men['middle_name'].append(name_list[2])


def create_person(men, women):
    for i in range(100):
        key = random.choice((names_of_men, names_of_women))
        person = {
            'name': random.choice(key['last_name']) + ' ' + random.choice(key['first_name']) + ' ' + random.choice(
                key['middle_name']),
            'city': random.choice(cities),
            'credit_card': random.choice(service),
            'deposit': random.choice(service),
            'mortgage': random.choice(service)
        }
        yield person


with open('results.txt', 'w', encoding='utf-8') as f:
    for key in create_person(names_of_men, names_of_women):
        for item in key:
            f.writelines('%s \t' % key[item])
        f.writelines('\n')
