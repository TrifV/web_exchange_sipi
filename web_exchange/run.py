"""
Точка входа для запуска Flask-приложения.
Запускает приложение в режиме отладки для разработки.
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Запуск Flask-сервера с включённым debug-режимом
    app.run(debug=True)