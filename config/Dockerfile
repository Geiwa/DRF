# bспользуйте базовый образ Python
FROM python:3.9
# Устанавливаем переменные среды
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /code

# Копируем файлы зависимостей
COPY requirements.txt /code/

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем проект в контейнер
COPY . /code/

# Запускаем команду для миграции базы данных
RUN python manage.py migrate

# Открываем порт, если ваше приложение слушает определенный порт
EXPOSE 8000

# Запускаем команду для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

