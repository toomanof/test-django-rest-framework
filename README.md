Тестовое приложение:
Задача: реализовать API, позволяющее добавлять, изменять, просматривать и удалять данные в модели "Приложения".
"Приложения" – это модель, которая хранит в себе внешние источники, которые будут обращаться к API. Обязательные поля модели: ID, Название приложения, Ключ API. Поле "Ключ API" нельзя менять через API напрямую, должен быть метод, позволяющий создать новый ключ API.
После добавления приложения – должна быть возможность использовать "Ключ API" созданного приложения для осуществления запросов к метод /api/test, метод должен возвращать JSON, содержащий всю информацию о приложении.

Использовать следующие технологии: Django 2.2.7, Django REST framework.

Разворачивание на сервере:

Вначале рекомендуется настроить virtualenv для работы перед настройкой зависимостей.

1. pip install -r requirements.txt
2. cd test_app
3. ./manage.py migrate
4. ./manage.py createsuperuser
5. В административной панели можно создавать приложения на странице "Приложения"

Тестирование производится с помощью:
    ./manage.py test


URL API
api/applications/ - вывод списка всех приложений

api/create_token/ - генерация нового API ключа  с обязательной передачей в запросе, параметром api_key, значение старого ключа

api/test/<api_key>/ - информаци я по приложению с указанием в url ключа API
