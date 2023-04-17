# Проект "Социальная сеть"

Серверная часть для приложения Социальная сеть.<br> 
Имеются 3 модели.<br> 
Это модели "Пользователи" (User); "Публикации" (Publications); и "Комментария" (Comments).
 
## Стек технологий

> - Python 3.8+
> - Django 3+ 
> - DRF 3.10+ 
> - База данных PostgreSQL 10+


## Создана учетная запись админа

> - логин: 
> - пароль: 

## Чтобы подключиться к базе данных выполните в терминале следующую команду:
```
docker run --name db_social_network -e POSTGRES_PASSWORD=default12345 -e POSTGRES_USER=admin -e POSTGRES_DB=db_social_network -p 5432:5432 -d postgres
```

Все зависимости есть в файле requirements.txt.

## Чтобы запустить проект локально:
```
1. Выполните команду: 
- pip install -r requirements.txt

2. Запустите Docker контейнер с бд:
- docker run --name db_social_network -e POSTGRES_PASSWORD=default12345 -e POSTGRES_USER=admin -e POSTGRES_DB=db_social_network -p 5432:5432 -d postgres

3. Создайте миграции:
- python manage.py makemigrations

4. Примените созданные миграции:
- python manage.py migrate

5. Запустите проект:
- python manage.py runserver
```
<br>
<br>
Также созданы сериализаторы на каждую из моделей. (Файлы в serializers > author.py; books.py; и reader.py)<br>
И представления на каждую из моделей. (Файлы в views > author.py; books.py; и reader.py)<br>


Юлия Гареева<br>
18.04.2023