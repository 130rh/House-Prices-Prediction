# Используем официальный образ Python 3.11 в качестве базового
FROM python:3.11

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем необходимые файлы в контейнер
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY model.pkl model.pkl

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 5000
EXPOSE 5000

# Запускаем Flask-приложение
CMD ["python", "app.py"]
