Автотесты для проверки функционала отправки письма с mail.google.com и несколько тестов на проверку API

Требования по тестам WEB UI
-------------

- Присутствие параметризация
- Проверка доступности хоста
- Логин и логаут вынесены в отдельную фикстуру
- Выполнение в двух браузерах
- Результаты теста должны быть визуализированы в отчете.

Требования по тестам API
-------------

- GET
 http://localhost:8080/test-api
Ответ от сервиса на запрос;{"name": "testName","count": 1,"priority": true}

- POST
 http://localhost:8080/test-api/{id}
Тело запроса:{"test": "auto","log": true }
Ответ от сервиса на запрос
{"testId": 1, "testType": "auto", "log": true}


Необходимый софт
-------------
- Install Docker
- Install and run selenoid
  - https://aerokube.com/selenoid/latest/

