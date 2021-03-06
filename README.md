# Замок IF

![](https://github.com/arsensokolov/castle-if.ru/blob/master/static/images/ban_castle.jpeg?raw=true)

![Website](https://img.shields.io/website?url=http%3A%2F%2Fcastle-if.ru)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/arsensokolov/castle-if.ru)

Это не оригигнальный код чата, это написанный полностью с нуля. Я постарался восстановить первозданный вид чата,
но чувствую, не все я вспомнил как оно было и не все получилось сделать аутентично.

Приходится собирать по крупинкам тот самый чат, было конечно здорово, если бы вдруг у кого-нибудь завалялся mhtml/mhtm 
файлы самого чата, раньше их можно было сделать используя Internet Explorer. У меня нет контактов первых создателей 
чата, поэтому если кто-то напишет мне их или кто-то из них отзовётся, будут очень благодарен.

### Минусы

- [x] Отсутствует поддержка кодировки Windows 1251.
- [x] Пришлось добавить cookies.
- [x] Большинство функций не работают без JS.

### Плюсы

- [x] Поддержка сессий, невозможно авторизоваться в чате под другим пользователем.
- [x] Простая масштабируемая административная панель.
- [x] Поддержка UTF-8.


## Установка на сервер

> Возможно кому-то, например мне в будущем, пригодится данная инструкция.

Скачаем репозиторий локально на сервер:

```bash
$ git clone https://github.com/arsensokolov/castle-if.ru.git
$ cd castle-if.ru/
```

Установим зависимости (Pipenv уже должен быть установлен на сервере):

```bash
$ pipenv install --system
$ pipenv shell
```

Развернем БД:

```bash
$ ./manage.py migrate
$ ./manage.py loaddata default_rooms
$ ./manage.py loaddata --app djantimat initial_data
$ ./manage.py createsuperuser
```

Все! Далее надо настроить HTTP сервер — это уже тривиально.!)))