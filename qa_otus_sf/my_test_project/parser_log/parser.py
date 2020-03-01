import argparse
import re
import json
import os

def parsing(path):
    with open(path) as file:
        for index, line in enumerate(file.readlines()):
            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
            method = re.search(r"\] \"(POST|GET|PUT|DELETE|HEAD)", line).groups()[0]
            if dict_ip.get(ip, None) is None:
                dict_ip[ip] = {
                    "GET": 0,
                    "POST": 0,
                    "PUT": 0,
                    "DELETE": 0,
                    "HEAD": 0,
                }
            if index < 10:
                print(ip)
            dict_ip[ip][method] += 1
        # print(dict_ip)
        count = 0
        all_method = {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0, 'HEAD': 0}
        for ip in dict_ip:
                # print(dict_ip[ip])
                for method in dict_ip[ip]:
                    all_method[method] += dict_ip[ip][method]
                    # print(method, dict_ip[ip][method])
                    count += dict_ip[ip][method]
        print('Всего запросов: ' + str(count))
        for key in all_method:
            print(key, all_method[key], end='; ')

        print(json.dumps(dict_ip, indent=4))

parser = argparse.ArgumentParser()
parser.add_argument('-f', dest='file', action='store', help='Path to log file')
parser.add_argument('-p', dest='parse', action='store_true', help='Write "-p" if you want parse all log files')
args = parser.parse_args()

dict_ip = {}
path_to_file = []

try:
    if os.path.isdir(args.file):
        if args.parse:
            print('Парсим все логи')
            for root, dirs, files in os.walk(args.file):
                for file in files:
                    if file.endswith('.log'):
                        path_to_file.append(os.path.join(root, file))
                print('Найденные файлы логов по указанному пути: ')
                print(path_to_file)
            for path in path_to_file:
                print('Логи из файла ' + path)
                parsing(path)
        else:
            print('Передан путь до каталога, введите путь до конкретного файла или ключ -p для поиска всех файлов')
            print('Все файлы каталога: ')
            print(os.listdir(args.file))
    else:
        try:
            if args.parse:
                print('Передан путь до конкретного файла, флаг -р не отработает')
            print('Логи из файла ' + args.file)
            parsing(args.file)
        except Exception as e:
            print('Что то пошло не так..')
            print(e)
            raise

except Exception as e:
    print('Небходимо передать путь до каталога/файла! Используйте ключ -f=your_path')
    print(e)
