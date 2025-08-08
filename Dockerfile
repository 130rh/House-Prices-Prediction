# Используем официальную Python картину
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем все файлы проекта в контейнер
COPY . /app

# Устанавливаем все зависимости из requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Открываем порт 8501
EXPOSE 8501

# Команда для запуска приложения
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
