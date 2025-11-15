# 5. Базовый образ Python
FROM python:latest

# Рабочая директория внутри контейнера
WORKDIR /app

# Сначала копируем зависимости
COPY requirements.txt .

# 6. Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY memory_info.py .

# Команда по умолчанию — запуск скрипта
CMD ["python", "memory_info.py"]
