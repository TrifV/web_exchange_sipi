Spekulit — Веб-приложение прогнозирования курса ценных бумаг

1. О проекте

Название: Spekulit (АС-Спекулит)

Описание: Spekulit — это биржевое веб-приложение для анализа фондового рынка и прогнозирования динамики цен на основе данных Московской биржи и моделей искусственного интеллекта.

Зачем: Проект помогает трейдерам, инвесторам и аналитикам быстро принимать обоснованные финансовые решения благодаря актуальным котировкам, техническим индикаторам и предсказаниям трендов.

⸻

2. Технологии и стек

Компонент	Технология
Язык	Python 3.x
Веб-фреймворк	Flask
Шаблонизатор	Jinja2
Фронтенд	HTML, CSS, JavaScript, Bootstrap
HTTP/API	requests
Визуализация	Plotly
Тестирование	pytest
Кэширование и защита	Flask-Caching, Flask-Limiter
БД	SQLite (прототип), PostgreSQL/MySQL (продакшн)
Контейнеризация	Docker (опционально)
CI/CD	GitHub Actions



⸻

3. Установка и запуск

Требования
	•	Python 3.8+
	•	Git
	•	(опционально) Docker & Docker Compose

Локальная установка

# 1. Клонировать репозиторий
git clone https://github.com/YourUsername/Spekulit.git
cd Spekulit

# 2. Создать и активировать виртуальное окружение
python3 -m venv venv
source venv/bin/activate   # для Linux/macOS
venv\Scripts\activate    # для Windows

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Настроить переменные окружения
cp .env.example .env
# Отредактируйте .env: ключи API, настройки БД, параметры кэша

# 5. Запустить приложение
flask run --host=0.0.0.0 --port=5000

С Docker

# Построить образ
docker build -t spekulit:latest .

# Запустить в контейнере
docker run -d --name spekulit -p 5000:5000 \
  --env-file .env spekulit:latest

или с Docker Compose:

version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    env_file: .env
    volumes:
      - .:/app

docker-compose up -d



⸻

4. Примеры использования
	1.	Открыть в браузере: http://localhost:5000
	2.	Выбрать стартовый пресет или настроить фильтры вручную
	3.	Просмотреть интерактивные графики цен и прогнозов

Demo: https://spekulit.example.com (скоро в сети)

⸻

5. Структура проекта

Spekulit/
├── app/
│   ├── static/
│   ├── templates/
│   ├── routes.py
│   └── models.py
├── docs/
│   └── images/
├── tests/
├── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md



⸻

6. Планы и развитие

TODO:
	•	Авторизация и управление портфелем
	•	Расширенные индикаторы и сигналы технического анализа
	•	Мультивалютная и мультисценарная поддержка бирж
	•	Мобильная версия и PWA
	•	Notifications: оповещения о важных событиях

Мы приветствуем вклад: отправляйте pull request или открывайте issue!

⸻

7. Контакты
	•	GitHub: https://github.com/TrifV/web_exchange_sipi

⸻

8. Особенности оформления
	•	Светлая и тёмная тема (на очереди)
	•	Значки статуса сборки и лицензии в шапке
	•	Красивые кодовые блоки и таблицы
	•	Скриншоты и анимированные GIF в документации
	•	Таблицы для удобного восприятия
