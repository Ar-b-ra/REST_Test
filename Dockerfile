FROM python:latest
ENV HOST=localhost
ENV PORT=8000
RUN apt update -y && \
    apt upgrade -y && \
    apt install -y --no-install-recommends \
    python3-pip \
    apt autoremove -y && \
    rm -rf /var/lib/apt/lists/*
# Копирование файлов в рабочую директорию
COPY . /REST_Test
# Установка рабочей директории
WORKDIR /REST_Test
# Установка зависимостей
RUN pip3 install --upgrade pip && \
    pip3 install -r requirements/requirements.txt
# Запуск приложения
EXPOSE 8000
CMD ["python3", "app.py", "--host", "${HOST}", "--port", "${PORT}"]