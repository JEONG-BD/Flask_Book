from flask import Flask 
from pathlib import Path 
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__) 
    app.config.from_mapping(
        SCRET_KEY = '2AZSMss3p05QpbcY2hBsJ',
        SQLALCHEMY_DATABASE_URI = 
            f"sqlite:///{Path(__file__).parent.parent / 'local.sqllite'}", 
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        SQLALCHEMY_ECHO = True 
    )
    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    db.init_app(app)
    Migrate(app, db)
    return app 
     