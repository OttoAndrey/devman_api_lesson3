# Сокращение ссылок с помощью Bitly

Скрипт для сокращения ссылок с помощью сервиса [Bitly](https://bitly.com/).

Если передать скрипту уже сокращенную ссылку, то в ответ придет кол-во переходов по ней.


## Запуск

Для запуска скрипта вам понадобится Python третьей версии.

Скачайте код с GitHub.

Установите зависимости:

`pip install -r requirements.txt`

Запустите скрипт и передайте ссылку:

`python3 main.py https://github.com/`


## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `main.py` 
и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Необходимые переменные:
- `BITLY_TOKEN` — токен для обращения к Api Bitly. Можно получить в [кабинете](https://dev.bitly.com/docs/getting-started/authentication) Bitly


## Используемые библиотеки

* [requests](https://pypi.org/project/requests/) - для запросов к [Api](https://dev.bitly.com/api-reference) Bitly

* [python-dotenv](https://pypi.org/project/python-dotenv/) - для обращения к переменным окружения


## Цели проекта

Devman. API веб-сервисов. Третий урок.

Сайт реализован в рамках курса по Django на [devman](https://dvmn.org/modules/).
