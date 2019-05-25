
quiz_content = {'Заполните пробел: Для преобразования числа в строку выполните "___(100)"':'str',
                'Для преобразования строки в число выполните "___(100)"':'int',
                'Какой тип данных будет у переменной f, если f = 12 + 2.5?':'float',
                'Как в Python обозначается истина?':'True',
                'Цикл с пред-условием':'While',
                'Чему равна переменная b, если b = bool(51)?':'True',
                'Чему равно утверждение: (True or False) and True?': 'True',
                'Чему равно утверждение 0 == None?': 'False',
                'Что вернет выражение "Hello"[1]?':'e',
                'Что вернет выражение len("Hello world!")':'12'}
answers_counter = [0, 0]

for question in quiz_content.keys():
    answer = input(question)
    if answer.lower() == quiz_content.get(question).lower():
        print('Верно!')
        answers_counter[0] += 1
        answers_counter[1] += 1
    elif not answer.lower():
        print('Вопрос пропущен')
    else:
        print('Неправильно!')
        answers_counter[0] += 1
print("Дано ответов: {}, Верных ответов: {}".format(answers_counter[0], answers_counter[1]))