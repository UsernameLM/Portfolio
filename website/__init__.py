from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lapluma'     #cookie chave
    from .views import views
    from .bolsa import bolsa
    #from .projeto1 import save_image,create_graph
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(bolsa, url_prefix='/')
    return app
