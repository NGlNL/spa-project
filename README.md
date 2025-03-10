# Сервис по работе с привычками
Данный проект по управлению привычками пользователей. Он позволяет создавать, читать, обновлять и удалять привычки, а также получать публичные и приятные привычки. Функционал разработан с использованием Телеграм-бота, который отправляет ежедневные уведомления о привычках. В сервисе реализована регистрация и авторизация пользователей с соответствующим функционалом. Добавлен функционал работы с Docker, настроен процесс CI/CD с использованием GitHub Actions.
## Установка

1. Клонируйте репозиторий:

```bash
   git clone https://github.com/ваш-логин/ваш-репозиторий.git
   cd ваш-репозиторий
```

2. Создание и активация виртуального окружения:

Создайте виртуальное окружение:
```python3 -m venv venv```
Активируйте виртуальное окружение:
Для macOS и Linux:
```source venv/bin/activate```
Windows:
```venv\Scripts\activate```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Запустите сервер:
```bash
python manage.py runserver
```

# Использование:
Вам нужно будет зарегистрироваться и авторизоваться, после чего вы получите свой персональный токен, который нужно будет добавить в поле авторизации.
```bash
{
    "email": "почта",
    "password": "пароль"
}
```

```bash
Authorization: Bearer <token>
```

## Данные файла .env
Заполните файл ".env.sample" своими данными и переименуйте его в '.env'

## Celery

В этом проекте реализована функциональность для отправки уведомлений пользователям и управления  с использованием Celery и telegram

## Установка и настройка

1. Убедитесь, что у вас установлен Celery и необходимые зависимости.
2. Настройте SMTP сервер в файле конфигурации вашего проекта для отправки почты.
3. Запустите Celery worker и Celery Beat в отдельных терминалах:

   ```bash
   # Запуск worker
   celery -A config worker --loglevel=info

   # Запуск beat
   celery -A config beat --loglevel=info
   ```
## Docker

### Шаги для запуска

1. Убедитесь, что у вас установлен Docker
2. Скопируйте файл `.env.sample` в `.env` и заполните его вашими данными.
3. В корне проекта выполните команду:

   ```bash
   docker-compose up -d --build
   ```
4. После успешного запуска вы сможете проверить работоспособность сервисов:

Бэкенд: Перейдите по адресу http://localhost:8000
PostgreSQL: Подключитесь к базе данных на localhost:5432 с использованием указанных в .env данных.
Redis: Используйте redis-cli для подключения к localhost:6379.
Celery и Celery Beat: Логи можно просмотреть через docker-compose logs или подключившись к контейнерам.
### Остановка проекта
Чтобы остановить проект, выполните:
```bash
docker-compose down
````
# CI/CD для Django

Этот проект использует GitHub Actions для непрерывной интеграции и развертывания Django-приложения.

## Предисловие

1. **Репозиторий GitHub**: Создайте репозиторий на GitHub для своего Django-проекта.
2. **Учетная запись Docker Hub**: Создайте аккаунт на Docker Hub для pushes и pulls Docker-изображений.
3. **Удаленный сервер**: Настройте удаленный сервер с установленным Docker для развертывания приложения.
4. **Секреты**: Установите следующие секреты в настройках своего репозитория GitHub:
   - `SECRET_KEY`: Ключ секрета вашего Django-проекта.
   - `DOCKER_HUB_USERNAME`: Ваш логин на Docker Hub.
   - `DOCKER_HUB_ACCESS_TOKEN`: Личный токен доступа Docker Hub с правами чтения и записи.
   - `SSH_KEY`: Приватный ключ для доступа по SSH к вашему удаленному серверу.
   - `SSH_USER`: Логин для доступа по SSH к вашему удаленному серверу.
   - `SERVER_IP`: IP-адрес или hostname вашего удаленного сервера.
   - `DEPLOY_DIR`

## Настройка

1. **Создайте файл requirements.txt**: Перечислите все необходимые Python-пакеты для вашего Django-проекта в файле `requirements.txt`.
2. **Создайте Dockerfile**: В корневой директории проекта создайте файл `Dockerfile` с содержанием проекта.

Рабочий процесс GitHub Actions автоматически собирает, тестирует и развертывает ваше Django-приложение при push'е изменений в репозиторий или при создании pull request.

Рабочий процесс выполняет следующие задачи:

Лентинг (Linting): Запускает flake8 для проверки кода Python.
Тестирование: Настраивает окружение Python, устанавливает зависимости и запускает тесты с помощью python manage.py test.
Сборка: Собирает Docker-образ и отправляет его на Docker Hub.
Развертывание: Загружает Docker-образ с Docker Hub и запускает его на удаленном сервере по адресу: 158.160.155.146