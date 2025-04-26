"""
Фабрика приложения Flask.
Создаёт и настраивает приложение, регистрируя Blueprint-ы и необходимые расширения.
"""
from flask import Flask
import os

def create_app():
    """
    Создаёт экземпляр Flask-приложения и регистрирует маршруты.

    Returns:
        app (Flask): настроенный экземпляр приложения.
    """
    # Определяем папки для шаблонов и статических файлов внутри пакета
    template_folder = os.path.join(os.path.dirname(__file__), 'templates')
    static_folder = os.path.join(os.path.dirname(__file__), 'static')

    app = Flask(
        __name__,
        static_folder=static_folder,
        template_folder=template_folder
    )
    # Регистрируем основной blueprint
    from .routes import main
    app.register_blueprint(main)
    return app