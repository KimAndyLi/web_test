from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager
from flask_migrate import Migrate

from webapp.news.views import blueprint as news_blueprint
from webapp.weather import weather_by_city
from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


def create_app():
    #  Теперь запуск сервера происходит при помощи (писать в powershell построчно):
    # $env:FLASK_APP = "webapp" - импортируется во Flask webapp, запускается файл __init__.py, (см. выше) данный файл же является инициализацией Flask приложения
    # $env:FLASK_ENV = "development" - режим разработчика
    # $env:FLASK_DEBUG = 1 # активация дебаг мода (чтобы каждый раз не перезагружать сервер при кодинге)
    # flask run или python -m flask run - запуск flask
    app = Flask(__name__)  # Указание, что Flask приложение-данный файл
    app.config.from_pyfile("config.py")  # Указание для Flask откуда читать конфигурацию
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
