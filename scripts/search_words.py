import re
import sys

""" 
Необходимо реализовать консольную программу, которая бы считывала текстовый файл подаваемый на вход и на выходе показывала список уникальных слов без учета регистра и количество упоминаний слова в тексте:

1) в порядке уменьшения количества символов в слове. Если символов в слове будет одинаковое количество, нужно отсортировать их в алфавитном порядке.

2) в порядке часты встречания слова в тексте.

3) в алфавитном порядке

Аргументы:

path — путь до входного файла

output_order - тип сортировки слов при выводе.

top - параметр ограничивающий количество выдаваемых слов

Дополнительно:

filter - Добавить опциональный параметр, который должен позволять отфильтровать текст подаваемый на вход которые содержат слово передаваемое программе на вход в качестве аргумента. В качестве аргумента может быть задано не конкретное слово, но и регулярное выражение.


Варианты запуска

python search_words.py "D:\TDD\geckodriver.log" 1 200 "\d+"
 1 аргумент путь до файла - "D:\TDD\geckodriver.log"
 2 аргумент тип сортировки - 1 
 3 аргумент кол-во строчек вывода - 200
 4 опциональный аргумент (можно запускать без него) слово или регулярное выражение - "\d+"

"""

def main(filter):

    with open(sys.argv[1], "r") as f:
        text_string = f.read().lower()
        if filter:
            match_pattern = re.findall(filter, text_string)
        else:
            match_pattern = re.findall(r'\b[a-z]{1,}\b', text_string)

    frequency = {}
    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    if sys.argv[2] == '1': #1 decrease symbols
        print("В порядке уменьшения количества символов в слове")
        for i in sorted(frequency.items(), key=lambda x: (len(x[0]), x[0]))[:int(sys.argv[3])]:
            print(i[0], i[1])
    elif sys.argv[2] == '2': #2 frequency word in text
        print("В порядке частоты встречания слова в тексте")
        for words in sorted(frequency.items(), key=lambda x: x[1])[:int(sys.argv[3])]:
            print(words[0], words[1])
    elif sys.argv[2] == '3': #3 alphabet
        print("В алфавитном порядке")
        for words in sorted(frequency.keys())[:int(sys.argv[3])]:
            print(words, frequency[words])


if __name__ == '__main__':
    try:
        filter = sys.argv[4]
    except:
        filter = None
    main(filter)

