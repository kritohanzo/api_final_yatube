# Реализация API для проекта Yatube [FINAL]
Данный проект создан с целью обучения и практики реализации собственных API.
В данном случае, это API для проекта Yatube.
Возможно когда-то мы создадим SPA с использованием фронтенда и этого бекенда, кто знает...

# Запуск проекта на своём компьютере
Для всех последующих команд используйте терминал BASH.

Для начала клонируем репозиторий на свой компьютер:
```
git clone https://github.com/kritohanzo/api_final_yatube.git
```
Разворачиваем своё виртуальное окружение:
```
python -m venv venv
```
```
. venv/Scripts/activate
```
Далее устанавливаем зависимости, ведь без них ничего не заработает:
```
pip install -r requirements.txt
```
Выполняем миграции Django:
```
python manage.py migrate
```
Запускаем локальный сервер:
```
python manage.py runserver
```

# Примеры запросов к API.
Для создания нового пользователя можно обратиться по адресу с помощью POST-запроса, передав в тело запроса имя пользователя и пароль:
```
http://127.0.0.1:8000/api/v1/users/
```

Для получения токена после регистрации можно обратиться по адресу с помощью POST-запроса, передав в тело запроса имя пользователя и пароль:
```
http://127.0.0.1:8000/api/v1/jwt/create/
```

Для получения поста можно обратиться по адресу с помощью POST-запроса, передав в заголовок свой токен в формате «Bearer <token>», а в тело запроса текст нового поста:
```
http://127.0.0.1:8000/api/v1/posts/
```

Для получения списка всех постов можно обратиться по адресу с помощью GET-запроса, не передавая в заголовок свой токен:
```
http://127.0.0.1:8000/api/v1/posts/
```
